#Module used to automatically load level components - it might be necessary to modify in future if file system is changed

from modules import moduleLoader
from modules import moduleImageLoader
from modules import moduleDrawing

import os

#Constants
TERRAIN_FILE_NAME = "terrain.txt"
TERRAIN_ENCODING_FILE_NAME = "terrain_encoding.txt"
IMAGE_BIND_FILE_NAME = "image_bind.txt"
LEVEL_PLAYER_CONFIG_FILE_NAME = "level_player_config.txt"
ENEMY_TYPES_FILE_NAME = "enemy_types.txt"
TOWER_TYPES_FILE_NAME = "tower_types.txt"

def auto_load_level(level_path,TILE_SIZE,MAX_TERRAIN_SIZE=[]):    
    #Creates paths to files
    path_to_terrain = os.path.join(level_path,TERRAIN_FILE_NAME)
    path_to_terrain_encoding = os.path.join(level_path,TERRAIN_ENCODING_FILE_NAME)
    path_to_image_bind = os.path.join(level_path,IMAGE_BIND_FILE_NAME)

    #Loads files
    terrain = moduleLoader.load_terrain(path_to_terrain,MAX_TERRAIN_SIZE)
    terrain_encoding = moduleLoader.load_terrain_encoding(path_to_terrain_encoding)
    image_bind = moduleLoader.load_image_bind(path_to_image_bind)    

    #Loads images assigned to object/tile names
    name_to_image_dict = moduleImageLoader.auto_load_images(image_bind,path_to_terrain,TILE_SIZE)

    #Creates terrain surface to be blitted onto screen
    terrain_surface = moduleDrawing.create_terrain_surface(terrain,terrain_encoding,
                                                                name_to_image_dict,TILE_SIZE)

    return (terrain,terrain_encoding,image_bind,name_to_image_dict,terrain_surface)

def auto_load_level_player_config(any_path_in_game_folder):
    """Automatically finds file by ascending if possible and loads level player config"""
    #Ascends in file system until it finds folder with LEVEL_PLAYER_CONFIG_FILE_NAME name
    #or until it hits top most folder/file/drive
    tail = "true" #Folder on the end of the path
    path = any_path_in_game_folder
    
    while tail and not os.path.isfile(os.path.join(path,LEVEL_PLAYER_CONFIG_FILE_NAME)):
        path, tail = os.path.split(path) #Splits path into the path without tail and tail

    if not tail: #Folder with resources wasn't found
        raise IOError(str(LEVEL_PLAYER_CONFIG_FILE_NAME)+" was not found")
        return

    path = os.path.join(path,LEVEL_PLAYER_CONFIG_FILE_NAME)

    level_player_config = moduleLoader.load_level_player_config(path)

    return level_player_config

def auto_load_enemy_types(any_path_in_game_folder):
    """Automatically finds file by ascending if possible and loads level player config"""
    #Ascends in file system until it finds folder with ENEMY_TYPES_FILE_NAME name
    #or until it hits top most folder/file/drive
    tail = "true" #Folder on the end of the path
    path = any_path_in_game_folder
    
    while tail and not os.path.isfile(os.path.join(path,ENEMY_TYPES_FILE_NAME)):
        path, tail = os.path.split(path) #Splits path into the path without tail and tail

    if not tail: #Folder with resources wasn't found
        raise IOError(str(ENEMY_TYPES_FILE_NAME)+" was not found")
        return

    path = os.path.join(path,ENEMY_TYPES_FILE_NAME)

    enemy_types = moduleLoader.load_enemy_types(path)

    return enemy_types

def auto_load_tower_types(any_path_in_game_folder):
    """Automatically finds file by ascending if possible and loads level player config"""
    #Ascends in file system until it finds folder with TOWER_TYPES_FILE_NAME name
    #or until it hits top most folder/file/drive
    tail = "true" #Folder on the end of the path
    path = any_path_in_game_folder
    
    while tail and not os.path.isfile(os.path.join(path,TOWER_TYPES_FILE_NAME)):
        path, tail = os.path.split(path) #Splits path into the path without tail and tail

    if not tail: #Folder with resources wasn't found
        raise IOError(str(TOWER_TYPES_FILE_NAME)+" was not found")
        return

    path = os.path.join(path,TOWER_TYPES_FILE_NAME)

    tower_types = moduleLoader.load_enemy_types(path)

    return tower_types
