"""Module storing EnemyManager class used to control enemies."""
from operator import itemgetter #Used for fast tuples in list sorting. Will be used for pathfinding.
#data.sort(key=itemgetter(1))

class EnemyManager():
    """Class used to control and spawn all enemies."""
    def __init__(self,parent,terrain,terrain_encoding,
                 ENEMY_TYPES,enemy_waves,destination):
        self.parent = parent #Stores instance that initialized this class.

        self.terrain = terrain
        self.terrain_encoding = terrain_encoding

        self.ENEMY_TYPES = ENEMY_TYPES #Stores all types of enemies.
        self.waves = enemy_waves
        self.destination = destination #Stores position that is target of the enemies.
        
        self.enemies = [] #Stores all live enemies.

        self.paths = {} #Stores path to destination assigned to enemy types.

        self.current_wave = 0 #Stores integer indicating on which wave the player currently is.

    def find_path(self,enemy_type):
        """Finds path for target enemy type to the destination.

        It finds path by searching from the destination to one of
        the vertices of the terrain using A* pathfinding with all
        nodes having cost 1. Nodes in dictionary visited and in priority
        queue processing_queue will have format
        (x,y,distance_from_start,heuristic_value).
        
        First this function creates dictionary containing how to get
        from any point to destination if possible and then it uses
        this dictionary to create shortest path from the terrain vertex
        to the destination.
        """
        visited = {self.destination:()} #Stores already visited positions on the terrain.

        #distance_from_end = distance from the closest terrain vertex.
        distance_from_end = min([self.destination[0],self.destination[1],
                               len(self.terrain)-self.destination[0],len(self.terrain[1])-self.destination[1]])
        start_node = (self.destination[0],self.destination[1],0,distance_from_end+0) #Creates start node.

        processing_queue = [start_node] #Priority queue containing all nodes that should be processed.

        while processing_queue:
            #Sorts the processing_queue so nodes with lowest heuristic values are at the end.
            processing_queue.sort(key=itemgetter(3))
            processing_queue.reverse()

            current_node = processing_queue.pop() #Takes the node with lowest heuristic value from the queue.

            if ((current_node[0] == 0 or current_node[0] == len(self.terrain)-1) and
                (current_node[1] == 0 or current_node[1] == len(self.terrain[0])-1)):
                #Current node is at the vertex of the terrain, what means that goal is reached.
                #Pathfinding cycle will be ended because it is no longer required.
                break

            #Tuple of neighbouring nodes is created.
            neighbouring_nodes = ((current_node[0]-1,current_node[1]),(current_node[0]+1,current_node[1]),
                                  (current_node[0],current_node[1]-1),(current_node[0],current_node[1]+1))

            for node in neighbouring_nodes: #Iterates through all neighbouring nodes.
                if not node in visited: #Checks if the node hasn't been already visited
                    #Checks if the node position can be passed by that enemy type
                    if self.terrain_encoding[self.terrain[node[0]][node[1]]] in self.ENEMY_TYPES[enemy_type]["Can_cross"]:
                        #Obtains distance of the new node from the closest terrain vertex.
                        distance_from_end = min([node[0],node[1],
                                       len(self.terrain)-node[0],len(self.terrain[1])-node[1]])
                        
                        #Creates new node for processing_queue.
                        new_node = (node[0],node[1],current_node[2]+1,distance_from_end+current_node[2]+1)

                        visited[node] = (current_node[0],current_node[1])
                        processing_queue.append(new_node)

        #Creates the path itself.
        current_node = (current_node[0],current_node[1])
        path = []

        while current_node: #While the destination hasn't been reached.
            path.append(current_node) #Adds current_node to the path.
            current_node = visited[current_node] #Selects next node on the way to the destination.

        return path

    def create_enemy(self,enemy_type):
        """Creates new enemy at the proper position and adds it to the list."""
        try: #Checks if the path for that enemy type is in the dict of paths.
            self.paths[enemy_type]
        except KeyError: #If it wasn't found, it will be created.
            self.paths[enemy_type] = self.find_path(enemy_type)
            
        
    def logic_frame(self):
        """Logic frame of the EnemyManager."""
        #Part of the logic frame creating new enemies.
        if self.waves[self.current_wave] == []: #Current wave has been depleted so new one is started.
            self.current_wave += 1

        """Waves should be lists containing list with format [enemy_type, amount_of_enemies,
        time_required_to_spawn_the_enemy, starting_timer_value]"""

        for part_of_wave_position in range(len(self.waves[self.current_wave])):
            part_of_wave = self.waves[self.current_wave][part_of_wave_position]
            if not part_of_wave == []: #Checks if current part_of_wave has been deactivated, if yes, it is skipped.
                if part_of_wave[-1] >= part_of_wave[-2]: #Timer is higher or equal as the required time for new enemy.
                    part_of_wave[-1] = 1 #Resets the timer.
                    part_of_wave[1] -= 1 #Amount of enemies that can come from that part of wave is decreased.

                    self.create_enemy(part_of_wave[0]) #Creates new enemy of the proper type.
                    
                part_of_wave[-1] += 1 #Increases the timer value.

                if part_of_wave[1] <= 0: #All enemies from the current part has been depleted.
                    self.waves[self.current_wave][part_of_wave_position] = [] #Current part_of_wave is replaced with [].

        #Enemy actions - enemies are moving and updating...
        
    
    def drawing_frame(self):
        pass
    
