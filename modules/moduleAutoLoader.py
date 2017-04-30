#Module used to automatically load level components

from modules import moduleLoader
from modules import moduleImageLoader
from modules import moduleDrawing

import os

#Constants
TERRAIN_FILE_NAME = "terrain.txt"
TERRAIN_ENCODING_FILE_NAME = "terrain_encoding.txt"
IMAGE_BIND_FILE_NAME = "image_bind.txt"

def auto_load_level(level_path,TILE_SIZE):    
    #Creates paths to files
    path_to_terrain = os.path.join(level_path,TERRAIN_FILE_NAME)
    path_to_terrain_encoding = os.path.join(level_path,TERRAIN_ENCODING_FILE_NAME)
    path_to_image_bind = os.path.join(level_path,IMAGE_BIND_FILE_NAME)

    #Loads files
    terrain = moduleLoader.load_terrain(path_to_terrain)
    terrain_encoding = moduleLoader.load_terrain_encoding(path_to_terrain_encoding)
    image_bind = moduleLoader.load_image_bind(path_to_image_bind)    

    #Loads images assigned to object/tile names
    name_to_image_dict = moduleImageLoader.auto_load_images(image_bind,path_to_terrain,TILE_SIZE)

    #Creates terrain surface to be blitted onto screen
    terrain_surface = moduleDrawing.create_terrain_surface(terrain,terrain_encoding,
                                                                name_to_image_dict,TILE_SIZE)

    return (terrain,terrain_encoding,image_bind,name_to_image_dict,terrain_surface)
