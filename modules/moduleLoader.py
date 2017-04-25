#This module handles loading that is necessary for game

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

def load_terrain(path): #Loads terrain map, rectangle out of character representing tiles using terrain encoding
    """Terrain must contain characters forming rectangle. Each character represents one tile of the terrain.
    Commets are created by adding # at the beginning of the line
    """

    try:
        file = open(path, "r") #Opens file containing terrain map
    except IOError: #File wasn't found
        raise
        return "File cannot be opened"

    try:
        terrain = [] #Two dimensional list containing whole terrain map with each tile represented by one character
        
        for line in file: #Iterates over all lines in the file
            if not line[0] == "#": #The line is not a comment line
                if "\n" in line: #Removes line ending if it is in the line
                    line = line[:-1]

                terrain.append(list(line))
                

    finally: #Closes the file always, even when exception/error has occured
        file.close()

    return terrain

    
