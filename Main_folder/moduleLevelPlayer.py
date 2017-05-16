"""Module used to play levels"""
import pygame
from pygame.locals import *

from mini_modules import moduleGameClock

from modules import moduleDrawing
from modules import moduleAutoLoader

import os #Used mostly to work with paths.
import traceback #Used to print exceptions when using cmd.

import moduleEnemyManager #Used to control and spawn enemies.

#Color definition.
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
BLUE     = (   0,   0, 255)
VIOLET   = ( 128,   0, 127)
YELLOW   = ( 255, 255,   0)

#Names of constants.
TILE_SIZE = "TILE_SIZE"
MAX_TERRAIN_WIDTH = "MAX_TERRAIN_WIDTH"
MAX_TERRAIN_HEIGHT = "MAX_TERRAIN_HEIGHT"

LOGIC_CYCLE_INTERVAL = "LOGIC_CYCLE_INTERVAL" #Interval of logic cycles in miliseconds (1/1000 of the second).


class LevelPlayer():
    """Class used to load levels and play them."""
    def __init__(self,game_folder_path,real_screen=None):
        #Loads level player config - it will be constant dictionary with value assigned to KEYS because they are constants.
        self.CONFIG = moduleAutoLoader.auto_load_level_player_config(game_folder_path)

        #Loads level player GUI config.
        self.GUI_CONFIG = moduleAutoLoader.auto_load_level_player_GUI(game_folder_path)
        
        #Loads enemy types that will be then used when spawing enemies - again constant dictionary.
        self.ENEMY_TYPES = moduleAutoLoader.auto_load_enemy_types(game_folder_path)
        
        #Loads tower types that will be then used when building towers - again constant dictionary.
        self.TOWER_TYPES = moduleAutoLoader.auto_load_tower_types(game_folder_path)

        #real_screen creation - real_screen is pygame display shown to user.
        if not real_screen: #If real_screen hasn't been provided, pygame has to be initialized and real_screen created.
            pygame.init()

            #The window will be square with side length of half of the display dimesions.
            display_info = pygame.display.Info()
            self.real_screen_size = [display_info.current_w,display_info.current_h]
            smaller_dimension = min(self.real_screen_size)
            self.real_screen_size = (int(smaller_dimension/2),int(smaller_dimension/2))
            
            self.real_screen = pygame.display.set_mode(self.real_screen_size,RESIZABLE) #Real screen is the surface shown to user,
            #its size can be changed by user.
            
            pygame.display.set_caption("TD Level Player") #Sets caption.

        else:
            self.real_screen = real_screen

        #GUI creation.
        #screen is surface that is then scaled and blit onto the real screen - it has constant size.
        self.screen = pygame.Surface((self.GUI_CONFIG["screen"]["width"],self.GUI_CONFIG["screen"]["height"]))
        #game_screen is surface used to show terrain, towers, enemies... and is blit on the screen.
        self.game_screen = pygame.Surface((self.GUI_CONFIG["game_screen"]["width"],self.GUI_CONFIG["game_screen"]["height"]))

        #Money variable used to store how much money can be used to construct towers.
        self.money = 0
        #Lifes variable used to store how much "life" is remaining, decreased when emeny gets to the end.
        self.lifes = 100

        #Variable used to store towers currently on the game_screen.
        self.towers = []

        self.clock = moduleGameClock.GameClock(self.CONFIG[LOGIC_CYCLE_INTERVAL]) #Clock used to regulate FPS and to hold constant game speed.
        self.fps_limit = 60 #Limits FPS to prevent unnecessary usage of CPU/GPU.

    def logic_frame(self):
        """Used to process user input and advance game state."""
        #User events processing.
        for event in pygame.event.get():
            if event.type == QUIT:
                self.cycle = False
                
            if event.type == VIDEORESIZE: #Gets the event when user resizes the window.
                self.real_screen_size = (event.w,event.h)
                self.real_screen = pygame.display.set_mode(self.real_screen_size,RESIZABLE)
                
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self.cycle = False

            if event.type == MOUSEBUTTONDOWN:
                #When mouse button is pressed, mouse_position is obtained.
                mouse_position = pygame.mouse.get_pos()
                #mouse_position is divided by the size of real screen and then multipled by size of draw screen.
                mouse_position = (mouse_position[0]/self.real_screen_size[0]*self.GUI_CONFIG["screen"]["width"],
                                  mouse_position[1]/self.real_screen_size[1]*self.GUI_CONFIG["screen"]["height"])

        #End of user events processing.
        self.enemyManager.logic_frame()

    def drawing_frame(self):
        """Used to draw and show everything to the user."""
        self.screen.fill(BLACK) #Fills the screen with BLACK color.

        #game_screen drawing.
        self.game_screen.fill(BLACK) #Fills the game_screen  with BLACK color.
        self.game_screen.blit(self.terrain_surface,(0,0)) #Blits terrain on the game_screen.

        self.enemyManager.drawing_frame() #Calls EnemyManager drawing frame to draw enemies.

        #Blits the game_scren on the screen.
        self.screen.blit(self.game_screen,(self.GUI_CONFIG["game_screen"]["posX"],self.GUI_CONFIG["game_screen"]["posY"]))
        
        pygame.transform.scale(self.screen,self.real_screen_size,self.real_screen) #Scales and blits screen on the display.
        
        pygame.display.flip() #Flips the real screen into window so it will be visible to the user.
        self.clock.tick(self.fps_limit) #Makes game clock now that one drawing frame has passed and sets FPS limit.

    def run(self,level_path):
        """Used to load and play level."""
        #Uses auto_load() from moduleAutoLoader to load everything automatically.
        loaded = moduleAutoLoader.auto_load_level(level_path,self.CONFIG[TILE_SIZE],
                                                  (self.CONFIG[MAX_TERRAIN_WIDTH],self.CONFIG[MAX_TERRAIN_HEIGHT]))
        self.terrain, self.terrain_encoding, self.image_bind = loaded[:3]
        self.name_to_image_dict, self.terrain_surface = loaded[3:]

        #Initializes EnemyManager for managing enemies.
        self.enemyManager = moduleEnemyManager.EnemyManager(self,self.terrain,self.terrain_encoding)
        
        #Program cycle
        try:
            self.cycle = True
            
            while self.cycle == True:
                for logic_frame_number in range(self.clock.update()): #Runs as many logic frames as is necessary to keep up.
                    self.logic_frame()
                self.drawing_frame()
                
        finally: #If the program finishes successfully or has unhandled exception, the pygame window will be closed.
            pygame.quit()



if __name__ == "__main__": #Program automatically runs only when directly launched.
    #Currently loads only Level_1.
    try:
        levelPlayer = LevelPlayer(os.path.join(os.getcwd(),"Example_Game"))
        levelPlayer.run(os.path.join(os.getcwd(),"Example_Game","Levels","Example_level"))
    except:
        traceback.print_exc()
    input("Press ENTER to end the program")

