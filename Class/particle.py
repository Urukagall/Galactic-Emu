import pygame

class Particle():
    def __init__(self, coordinates, radius, color):
        self.coordinates = coordinates
        self.radius = radius
        self.color = color
        self.layers = 3
        self.TTL = 300
    
    '''creates a circle'''
    def circle_surf(radius, color):
        surf = pygame.Surface((radius*2, radius*2))
        pygame.draw.circle(surf, color, (radius, radius), radius)
        #dont return the black background of the surface
        surf.set_colorkey((0,0,0))
        return surf

    def draw(self, screen):
        particleColor = self.color
        radius = self.TTL * 2
        for circle in range(self.layers):
            self.circle_surf(self.radius, particleColor)
