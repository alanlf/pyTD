"""Module containing GameClock class that is used to separate
logic cycles from drawing cycles"""
import pygame #Uses pygame.time.Clock() to measure time and passed drawing cycles

class GameClock():
    def __init__(self,interval):
        self.interval = interval #Interval of logic cycle in miliseconds
        self.timeclock = pygame.time.Clock() #Necessary to measure time
        self.time = 0 #Time passed (in miliseconds) - time counter
        
    def tick(self,fps_limit = 0):
        """Must be called at the end of drawing cycle, measures time and limits FPS.

        Replaces pygame.time.Clock.tick() in drawing cycle. Adds time passed from
        last call to the time counter. fps_limit is used to limit FPS using
        pygame.time.Clock.tick()."""
        #pygame.time.Clock.tick() - counts the time passed from the last drawing frame
        self.time += self.timeclock.tick(fps_limit)
        
    def update(self):
        """Returns how many logic cycles should run to keep constant game speed.

        It is calculated by dividing passed time by logic cycle interval. After
        that, required amount of logic cycles is multiplied by interval and
        substracted from the time counter."""
        required_update_count = int(self.time / self.interval)
        self.time -= self.interval*required_update_count #Decreases self_time
        return required_update_count
    
    def get_fps(self):
        """Returns FPS."""
        return self.timeclock.get_fps()
    
