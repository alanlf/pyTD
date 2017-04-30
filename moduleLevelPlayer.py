#Module used to play levels
import pygame
from pygame.locals import *

from mini_modules import moduleGameClock
from mini_modules import moduleFileDialog #Contains function file_dialog() used to select file using GUI

from modules import moduleDrawing
from modules import moduleAutoLoader

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

class LevelPlayer():
    def __init__(self):
        pygame.init()

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

    def drawing_frame(self):
        self.screen.fill(black) #Fills the screen with black color

        self.screen.blit(self.terrain_surface,(0,0))

        #End of the drawing frame
        pygame.transform.scale(self.screen,self.screen_size,self.real_screen)
        pygame.display.flip() #Flips the real screen into window so it will be visible to the user
        self.clock.tick(self.fps_limit) #Makes game clock now that one drawing frame has passed and sets FPS limit

    def run(self,level_path):
        #Uses auto_load() from moduleAutoLoader to load everything automatically
        loaded = moduleAutoLoader.auto_load_level(level_path,TILE_SIZE)
        self.terrain, self.terrain_encoding, self.image_bind = loaded[:3]
        self.name_to_image_dict, self.terrain_surface = loaded[3:]
        
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
    levelPlayer = LevelPlayer()
    levelPlayer.run("C:\\Prakticky-Vsetko\\Python_programovanie\\newTD\\Example_Game\\Levels\\Level_1")
