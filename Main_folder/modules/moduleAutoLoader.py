"""Module used to automatically find load files for other modules.

If file system is modified, this module might require modifications
to be functional."""
from modules import moduleLoader
from modules import moduleImageLoader
from modules import moduleDrawing

import os

#File names used when automatically loading, they might require changes in future
TERRAIN_FILE_NAME = "terrain.txt"
TERRAIN_ENCODING_FILE_NAME = "terrain_encoding.txt"
IMAGE_BIND_FILE_NAME = "image_bind.txt"
LEVEL_PLAYER_CONFIG_FILE_NAME = "level_player_config.txt"
LEVEL_PLAYER_GUI_FILE_NAME = "level_player_GUI.txt"
ENEMY_TYPES_FILE_NAME = "enemy_types.txt"
TOWER_TYPES_FILE_NAME = "tower_types.txt"

def auto_load_level(level_path,TILE_SIZE,MAX_TERRAIN_SIZE=[]): #@todo clean up
    """Automatically loads some parts of level."""
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

def auto_ascension_file_search(starting_path,target_file_name):
    """Automatically finds specified file by ascending. Returns path.

    Raises FileNotFoundError if specified file wasn't found."""
    tail = "TAIL_STRING"
    path = starting_path
    
    while tail and not os.path.isfile(os.path.join(path,target_file_name)):
        path, tail = os.path.split(path) #Splits path into the path without tail and tail

    if not tail: #Specified file wasn't found
        raise FileNotFoundError(str(target_file_name)+" was not found")
        return

    path = os.path.join(path,target_file_name)

    return path

def auto_load_level_player_config(any_path_in_game_folder):
    """Automatically loads level player config."""
    path = auto_ascension_file_search(any_path_in_game_folder,LEVEL_PLAYER_CONFIG_FILE_NAME)
    level_player_config = moduleLoader.load_level_player_config(path)

    return level_player_config

def auto_load_level_player_GUI(any_path_in_game_folder):
    """Automatically loads level player GUI."""
    path = auto_ascension_file_search(any_path_in_game_folder,LEVEL_PLAYER_GUI_FILE_NAME)
    level_player_GUI = moduleLoader.load_level_player_config(path)

    return level_player_GUI

def auto_load_enemy_types(any_path_in_game_folder):
    """Automatically loads enemy types."""
    path = auto_ascension_file_search(any_path_in_game_folder,ENEMY_TYPES_FILE_NAME)
    enemy_types = moduleLoader.load_enemy_types(path)

    return enemy_types

def auto_load_tower_types(any_path_in_game_folder):
    """Automatically loads tower types."""
    path = auto_ascension_file_search(any_path_in_game_folder,TOWER_TYPES_FILE_NAME)
    tower_types = moduleLoader.load_enemy_types(path)

    return tower_types
