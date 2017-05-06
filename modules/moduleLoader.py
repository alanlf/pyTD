#This module handles some of the loading that is necessary for game

import json #Used to load json files

#Custom exceptions/errors
class TerrainHasWrongSizeError(Exception):
    pass

def load_terrain_encoding(path): #Loads terrain encoding - tile names assigned to terrain map characters
    """Terrain encoding file must contain terrain map character:tile name pairs.
    Inside the pair, those 2 strings have to be separated by : and each pair must end with ;
    Commets are created by adding # at the beginning of the line
    """
    
    try:
        file = open(path, "r") #Opens file containing terrain encoding
    except IOError: #File wasn't found
        raise
        return "File cannot be opened"

    try:
        terrain_encoding = {} #Dictionary that stores terrain map character:tile name pairs
        
        for line in file: #Iterates over all lines in the file
            if not line[0] == "#": #The line is not a comment line
                if "\n" in line: #Removes line ending if it is in the line
                    line = line[:-1]

                line = line.split(";") #Splits the line at each ; to create pair strings 

                for pair in line:
                    if pair: #Pair string is not empty
                        pair = pair.split(":") #Splits the pair string into 2 components (terrain map character:tile name)
                        terrain_encoding[pair[0]] = pair[1] #Adds the pair into dictionary
            

    finally: #Closes the file always, even when exception/error has occured
        file.close()

    return terrain_encoding
        

def load_image_bind(path): #Loads image bind - image names assigned to object/tile names
    """Image bind must contain object/tile name:image name pairs
    Inside the pair, those 2 strings have to be separated by : and each pair must end with ;
    Commets are created by adding # at the beginning of the line
    """
    
    try:
        file = open(path, "r") #Opens file containing image bind
    except IOError: #File wasn't found
        raise
        return "File cannot be opened"

    try:
        image_bind = {} #Dictionary that stores object/tile name:image name pairs
        
        for line in file: #Iterates over all lines in the file
            if not line[0] == "#": #The line is not a comment line
                if "\n" in line: #Removes line ending if it is in the line
                    line = line[:-1]

                line = line.split(";") #Splits the line at each ; to create pair strings 

                for pair in line:
                    if pair: #Pair string is not empty
                        pair = pair.split(":") #Splits the pair string into 2 components (object/tile name:image name)
                        image_bind[pair[0]] = pair[1] #Adds the pair into dictionary
            

    finally: #Closes the file always, even when exception/error has occured
        file.close()

    return image_bind

def load_terrain(path,MAX_TERRAIN_SIZE=[]): #Loads terrain map, rectangle out of characters representing tiles using terrain encoding
    """Terrain must contain characters forming rectangle. Each character represents one tile of the terrain.
    Commets are created by adding # at the beginning of the line
    """
    #MAX_TERRAIN_SIZE is iterable containing width and height of terrain in tiles, all terrains must be of that size

    try:
        file = open(path, "r") #Opens file containing terrain map
    except IOError: #File wasn't found or cannot be opened
        raise
        return "File cannot be opened"

    try:
        terrain = [] #Two dimensional list containing whole terrain map with each tile represented by one character
        
        for line in file: #Iterates over all lines in the file
            if not line[0] == "#": #The line is not a comment line
                if "\n" in line: #Removes line ending if it is in the line
                    line = line[:-1]

                terrain.append(list(line))

        if MAX_TERRAIN_SIZE and (len(terrain) != MAX_TERRAIN_SIZE[1] or len(terrain[0]) != MAX_TERRAIN_SIZE[0]): #terrain has wrong size, error is raised
            raise TerrainHasWrongSizeError()
                

    finally: #Closes the file always, even when exception/error has occured
        file.close()

    return terrain

def load_level_player_config(path):
    """Loads level player configuration into dictionary.

    It opens file using the path provided and loads
    everything infront of = as key and behind it as value
    """

    try:
        file = open(path, "r") #Opens file containing level_player_config
    except IOError: #File wasn't found or cannot be opened
        raise
        return "File cannot be opened"

    try:
        level_player_config = {}
        
        for line in file: #Iterates over all lines in the file
            if not line[0] == "#": #The line is not a comment line
                if "\n" in line: #Removes line ending if it is in the line
                    line = line[:-1]

                line = line.replace(" ","") #Removes spaces from the line
                key, value = line.split("=") #Splits the line on the = character, string before is key, string after value

                #Tries to convert value to int
                try:
                    value = int(value)
                except ValueError:
                    pass
                
                level_player_config[key] = value #Puts the value assigned to key into dictionary

    finally: #Closes the file always, even when exception/error has occured
        file.close()

    return level_player_config

def load_enemy_types(path):
    """Loads enemy types from JSON file specified by path"""
    with open(path,"r") as file:
        enemy_types = json.load(file)

    return enemy_types

def load_tower_types(path):
    """Loads tower types from JSON file specified by path"""
    with open(path,"r") as file:
        tower_types = json.load(file)

    return tower_types
    
