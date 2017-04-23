#Used to separate logic frames from drawing frames
import pygame

class GameClock():
    def __init__(self,interval):
        self.interval = interval #Interval of logic cycle in miliseconds
        self.timeclock = pygame.time.Clock() #Necessary to measure time
        self.time = 0 #Time passed (in miliseconds)
    def tick(self,fps_limit = 0): #Used at end of drawing frame instead of pygame Clock
        #pygame.time.Clock.tick() - counts the time passed from the last drawing frame
        #fps_limit allows to limit fps
        self.time += self.timeclock.tick(fps_limit)
    def update(self): #Returns how many times should the logic cycle be called
        required_update_count = int(self.time / self.interval)
        self.time -= self.interval*required_update_count #Decreases self_time
        return required_update_count
    def get_fps(self): #Returns FPS
        return self.timeclock.get_fps()
    
