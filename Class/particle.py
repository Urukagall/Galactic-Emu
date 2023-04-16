import pygame

class Particle():
    def __init__(self, coordinates, radius, color, particleList):
        self.coordinates = coordinates
        self.radius = radius
        self.maxRadius = 1100
        self.color = color
        self.TTL = 100
        self.particleList = particleList
        self.particleList.append(self)

    def draw(self, screen, projectileList=[]):
        if(self.TTL <= 0):
            return True
        pygame.draw.circle(screen, self.color, self.coordinates, self.radius)
        glowRadius = self.radius + 100
        screen.blit(self.draw_particle(glowRadius, (20,20,20)), (self.coordinates.x - glowRadius, self.coordinates.y - glowRadius), special_flags = pygame.BLEND_RGB_ADD)
        if self.radius < self.maxRadius:
            self.radius += 20
        self.TTL -= 1
        projectileList.clear()
        return False

    def draw_particle(self, radius, color):
        surf = pygame.Surface((radius * 2, radius* 2))
        pygame.draw.circle(surf, color, (radius, radius), radius)
        surf.set_colorkey((0,0,0))
        return surf