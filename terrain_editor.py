#Program used to edit terrain #@todo change to module and integrate into primary editor
import pygame
from pygame.locals import *

from mini_modules import moduleGameClock
from mini_modules import moduleFileDialog #Contains function file_dialog() used to select file using GUI

from modules import moduleLoader
from modules import moduleImageLoader
from modules import moduleDrawing

import os #Used mostly to work with paths

#color definition
black    = (   0,   0,   0)
white    = ( 255, 255, 255)
green    = (   0, 255,   0)
red      = ( 255,   0,   0)
blue     = (   0,   0, 255)
violet   = ( 128,   0, 127)
yellow   = ( 255, 255,   0)

#Constants
TILE_SIZE = 64
DRAWING_SCREEN_SIZE = (640,640)
LOGIC_CYCLE_INTERVAL = 25 #Interval of logic cycles in miliseconds (1/1000 of the second)

TERRAIN_WINDOW = (0,0,640,640) #Top left corner and width and length of the window inside main window showing terrain

MOVE_UP_KEY = K_w
MOVE_DOWN_KEY = K_s
MOVE_LEFT_KEY = K_a
MOVE_RIGHT_KEY = K_d
MOVE_SPEED = TILE_SIZE/2

class TerrainEditor():
    def __init__(self,automatic_mode=True):
        pygame.init()

        self.automatic_mode = automatic_mode #Automatically loads additional required files after getting path of terrain map
        #If it is True, user has to choose terrain.txt file in the level folder and TerrainEditor will automatically
        #choose terrain_encoding.txt and image_bind.txt files (This works when path to terrain is provided as argument too)

        display_info = pygame.display.Info()
        self.screen_size = [display_info.current_w,display_info.current_h]
        smaller_dimension = min(self.screen_size)
        self.screen_size = (int(smaller_dimension/2),int(smaller_dimension/2))
        #The window will be square with side length of half of the display dimesions 
        self.real_screen = pygame.display.set_mode(self.screen_size,RESIZABLE) #Real screen is the surface shown to user - its size can be changed by user
        
        self.screen = pygame.Surface(DRAWING_SCREEN_SIZE) #Screen is surface that is then scaled and blit onto the real screen - it has constant size

        pygame.display.set_caption("TD Terrain Editor") #Sets caption

        self.clock = moduleGameClock.GameClock(LOGIC_CYCLE_INTERVAL) #Clock used to regulate FPS and to hold constant game speed
        self.fps_limit = 60 #Limits FPS to prevent unnecessary usage of CPU/GPU

        self.viewpoint = [0,0] #Used to move terrain around to manipulate terrains larger than screen

    def logic_frame(self):
        #User events processing
        for event in pygame.event.get():
            if event.type == QUIT:
                self.cycle = False
                
            if event.type == VIDEORESIZE: #Gets the event when user resizes the window
                self.screen_size = (event.w,event.h)
                self.real_screen = pygame.display.set_mode(self.screen_size,RESIZABLE)
                
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self.cycle = False

        pressed_keys = pygame.key.get_pressed() #Obtains pressed keys
        #Moves viewpoint
        if pressed_keys[MOVE_UP_KEY] and self.viewpoint[1] > 0:
            self.viewpoint[1] -= MOVE_SPEED
        if pressed_keys[MOVE_DOWN_KEY] and self.viewpoint[1] + TERRAIN_WINDOW[3] < len(self.terrain[0])*TILE_SIZE:
            self.viewpoint[1] += MOVE_SPEED
        if pressed_keys[MOVE_LEFT_KEY] and self.viewpoint[0] > 0:
            self.viewpoint[0] -= MOVE_SPEED
        if pressed_keys[MOVE_RIGHT_KEY] and self.viewpoint[0] + TERRAIN_WINDOW[2] < len(self.terrain)*TILE_SIZE:
            self.viewpoint[0] += MOVE_SPEED

    def drawing_frame(self):
        self.screen.fill(black) #Fills the screen with black color

        self.screen.blit(self.terrain_surface,(0-self.viewpoint[0],0-self.viewpoint[1]))

        #End of the drawing frame
        pygame.transform.scale(self.screen,self.screen_size,self.real_screen)
        pygame.display.flip() #Flips the real screen into window so it will be visible to the user
        self.clock.tick(self.fps_limit) #Makes game clock now that one drawing frame has passed and sets FPS limit

    def run(self,path_to_terrain_file=""):
        #Obtains required paths
        if self.automatic_mode: #Automatic/Semiautomatic mode
            if not path_to_terrain_file: #User has to choose file with terrain because it hasn't been provided as argument
                path_to_terrain_file = moduleFileDialog.file_dialog("Choose file with terrain")

            level_folder = os.path.dirname(path_to_terrain_file) #Obtains name of level folder in which the files are
            
            #Creates paths by adding terrain_encoding.txt and image_bind.txt to level folder
            path_to_terrain_encoding = os.path.join(level_folder,"terrain_encoding.txt")
            path_to_image_bind = os.path.join(level_folder,"image_bind.txt")

        else: #Manual mode
            #User has to choose file with terrain
            path_to_terrain_file = moduleFileDialog.file_dialog("Choose file with terrain")
            #Loads terrain_encoding and image_bind but user has to select them first
            path_to_terrain_encoding = moduleFileDialog.file_dialog("Choose file with terrain encoding")
            path_to_image_bind = moduleFileDialog.file_dialog("Choose file with image bind")

        #Loads terrain_encoding and image_bind
        self.terrain_encoding = moduleLoader.load_terrain_encoding(path_to_terrain_encoding)
        self.image_bind = moduleLoader.load_image_bind(path_to_image_bind)
        #Loads terrain - will be [] if it is new file - this shouldn't happen
        self.terrain = moduleLoader.load_terrain(path_to_terrain_file)

        #Loads images assigned to object/tile names
        self.name_to_image_dict = moduleImageLoader.auto_load_images(self.image_bind,path_to_terrain_file,TILE_SIZE)

        #Creates terrain surface to be blitted onto screen
        self.terrain_surface = moduleDrawing.create_terrain_surface(self.terrain,self.terrain_encoding,
                                                                    self.name_to_image_dict,TILE_SIZE)
        #Program cycle
        try:
            self.cycle = True
            
            while self.cycle == True:
                for logic_frame_number in range(self.clock.update()): #Runs as many logic frames as is necessary to keep up
                    self.logic_frame()
                self.drawing_frame()
                
        finally: #If the program finishes successfully or has unhandled exception, the pygame window will be closed
            pygame.quit()



if __name__ == "__main__":
    terrainEditor = TerrainEditor()
    terrainEditor.run("C:\\Prakticky-Vsetko\\Python_programovanie\\newTD\\Example_Game\\Levels\\Level_1\\terrain.txt")

    
