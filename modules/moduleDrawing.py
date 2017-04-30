#Module used to draw things and create surfaces
import pygame

def create_terrain_surface(terrain,terrain_encoding,name_to_image_dict,TILE_SIZE):
    """Returns terrain surface (used for blitting) of input terrain"""
    #terrain must be 2-dimensional iterable containing characters representing terrain tiles
    #terrain_encoding must be dictionary containing terrain character:tile name pairs
    #name_to_image_dict must be dictionary containing object/tile name:surface pairs
    #TILE_SIZE is integer constant indicating length of tile side

    terrain_surface = pygame.Surface((len(terrain)*TILE_SIZE,len(terrain[0])*TILE_SIZE))

    #Paints the terrain surface with tiles
    for x in range(len(terrain)):
        for y in range(len(terrain[x])):
            tile_to_blit = name_to_image_dict[terrain_encoding[terrain[x][y]]]
            terrain_surface.blit(tile_to_blit,(x*TILE_SIZE,y*TILE_SIZE))

    return terrain_surface
    
