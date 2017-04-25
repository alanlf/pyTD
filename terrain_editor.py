#Program used to edit terrain #@todo change to module and integrate into primary editor
import pygame
from pygame.locals import *

from mini_modules import moduleGameClock
from mini_modules import moduleFileDialog #Contains function file_dialog() used to select file using GUI

from modules import moduleLoader

import os #Used mostly to work with paths

#color definition
black    = (   0,   0,   0)
white    = ( 255, 255, 255)
green    = (   0, 255,   0)
red      = ( 255,   0,   0)
blue     = (   0,   0, 255)
violet   = ( 128,   0, 127)
yellow   = ( 255, 255,   0)

class TerrainEditor():
    def __init__(self,automatic_mode=True):
        pygame.init()

        self.automatic_mode = automatic_mode #Automatically loads additional required files after getting path of terrain map
        #If it is True, user has to choose terrain.txt file in the level folder and TerrainEditor will automatically
        #choose terrain_encoding.txt and image_bind.txt files (This works when path to terrain is provided as argument too)
        
        self.screen_size = (400,400) #Sets starting real screen size and constant drawing screen size
        self.real_screen = pygame.display.set_mode(self.screen_size,RESIZABLE) #Real screen is the surface shown to user - its size can be changed by user
        self.screen = self.real_screen.copy() #Screen is surface that is then scaled and blit onto the real screen - it has constant size

        pygame.display.set_caption("TD Terrain Editor") #Sets caption

        interval = 25 #Interval of logic cycles in miliseconds (1/1000 of the second)
        self.clock = moduleGameClock.GameClock(interval) #Clock used to regulate FPS and to hold constant game speed
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

        pygame.draw.polygon(self.screen,red,[[20,20],[60,300],[300,40]])

        #End of the drawing frame
        pygame.transform.scale(self.screen,self.screen_size,self.real_screen)
        pygame.display.flip() #Flips the real screen into window so it will be visible to the user
        self.clock.tick(self.fps_limit) #Makes game clock now that one drawing frame has passed and sets FPS limit

    def run(self,path_to_terrain_file=""):
        #Obtains required paths
        if self.automatic_mode: #Automatic/Semiautomatic mode
            if path_to_terrain_file:
                terrain_path = path_to_terrain_file
            else: #User has to choose file with terrain because it hasn't been provided as argument
                terrain_path = moduleFileDialog.file_dialog("Choose file with terrain")

            level_folder = os.path.dirname(terrain_path) #Obtains name of level folder in which the files are
            
            #Creates paths by adding terrain_encoding.txt and image_bind.txt to level folder
            path_to_terrain_encoding = os.path.join(level_folder,"terrain_encoding.txt")
            path_to_image_bind = os.path.join(level_folder,"image_bind.txt")

        else: #Manual mode
            #User has to choose file with terrain
            terrain_path = moduleFileDialog.file_dialog("Choose file with terrain")
            #Loads terrain_encoding and image_bind but user has to select them first
            path_to_terrain_encoding = moduleFileDialog.file_dialog("Choose file with terrain encoding")
            path_to_image_bind = moduleFileDialog.file_dialog("Choose file with image bind")


        
        #Loading itself
        #Loads terrain_encoding and image_bind
        self.terrain_encoding = moduleLoader.load_terrain_encoding(path_to_terrain_encoding)
        self.image_bind = moduleLoader.load_image_bind(path_to_image_bind)
        #Loads terrain - will be [] if it is new file
        self.terrain = moduleLoader.load_terrain(terrain_path)
        
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
    terrainEditor.run()

    
