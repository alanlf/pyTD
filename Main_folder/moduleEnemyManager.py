"""Module storing EnemyManager class used to control enemies."""
class EnemyManager():
    """Class used to control and spawn all enemies."""
    def __init__(self,parent,terrain,terrain_encoding):
        self.parent = parent #Stores instance that initialized this class.

        self.terrain = terrain
        self.terrain_encoding = terrain_encoding
        
        self.enemies = [] #Stores all live enemies.

        self.start_point = [] #Stores coordinates of tile on which enemies are spawned.
        self.path = {} #Stores path from starting point to the end.
        
    def logic_frame(self):
        pass
    
    def drawing_frame(self):
        pass
    
