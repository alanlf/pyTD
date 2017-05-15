"""Module used to load images and assign them to their names in dictionary"""
import pygame
import os

#@todo clean up and document some more

#Constants
RESOURCES_FOLDER_NAME = "Resources"

#Custom exceptions and errors
class FolderNotFoundError(Exception):
    pass

def load_images(image_bind,folder_path,TILE_SIZE):
    """Loads images from specified folder_path into dictionary in which
    they will be assigned to object/tile names coming from image_bind.
    image_bind dictionary has to contain object/tile name:image file name pairs.
    TILE_SIZE is constant representing length of side of one tile
    """
    #pygame display must be initialized before calling this function
    #because surface.convert_alpha() requires it
    #This means that this function should be called after using pygame.display.set_mode() atleast once

    name_to_image_dict = {} #Dictionary storing object/tile name:image (Surface) pairs

    error_surface = pygame.Surface((TILE_SIZE,TILE_SIZE))
    error_surface.fill((255,0,255)) #This surface is used in place of image if loading fails

    for name, image_name in image_bind.items():
        image_path = os.path.join(folder_path,image_name)

        try:
            image = pygame.image.load(image_path).convert_alpha() #Loads and converts the image
            image = pygame.transform.scale(image,(TILE_SIZE,TILE_SIZE)) #Scales the image to proper size
        except pygame.error:
            image = error_surface.copy() #If the image wasn't loaded, it will be replaced by error surface

        name_to_image_dict[name] = image

    return name_to_image_dict

def auto_load_images(image_bind,level_path,TILE_SIZE): #@todo move to moduleAutoLoader.py
    """Automatically finds folder by ascending with images if possible and loads images"""
    #Ascends in file system until it finds folder with RESOURCES_FOLDER_NAME name
    #or until it hits top most folder/file/drive
    tail = "true" #Folder on the end of the path
    path = level_path
    while tail and not os.path.isdir(os.path.join(path,RESOURCES_FOLDER_NAME)):
        path, tail = os.path.split(path) #Splits path into the path without tail and tail

    if not tail: #Folder with resources wasn't found
        raise FolderNotFoundError(str(RESOURCES_FOLDER_NAME)+" was not found")
        return

    path = os.path.join(path,RESOURCES_FOLDER_NAME)

    name_to_image_dict = load_images(image_bind,path,TILE_SIZE) #Loads the images using load_images()
    return name_to_image_dict
    

        
