import pygame

def darken(image, percent = 50):
    '''Creates a  darkened copy of an image, darkened by percent (50% by default)'''
    newImg = image.copy()
    dark = pygame.Surface(newImg.get_size()).convert_alpha()
    newImg.set_colorkey((0,0,0))
    dark.fill((0,0,0,percent/100*255))
    newImg.blit(dark, (0,0))
    return newImg