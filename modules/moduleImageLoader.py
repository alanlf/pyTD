#Module used to load images and assign them to their names in dictionary
import pygame
import os

def load_images(image_bind,folder,TILE_SIZE):
    """Loads images from specified folder into dictionary in which
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

    for name, image_name in image_bind:
        image_path = os.path.join(folder,image_name)

        try:
            image = pygame.image.load(image_path).convert_alpha()
        except pygame.error:
            image = error_surface.copy()

        name_to_image_dict[name] = image

    return name_to_image_dict

        
