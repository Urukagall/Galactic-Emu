import pygame

class Particle():
    def __init__(self, coordinates, radius, color, particleList):
        self.coordinates = coordinates
        self.radius = radius
        self.maxRadius = 1100
        self.color = color
        self.TTL = 120
        self.particleList = particleList
        self.particleList.append(self)
        self.reverse = False
        self.alpha = 255
        self.doDamage = False
        self.didDamage = False

    def draw(self, screen, projectileList=[]):
        
        if(self.TTL <= 0):
            return True
        if self.radius > 0:
            pygame.draw.circle(screen, self.color, self.coordinates, self.radius)
            glowRadius = self.radius + 100
            screen.blit(self.draw_particle(glowRadius, (20,20,20)), (self.coordinates.x - glowRadius, self.coordinates.y - glowRadius), special_flags = pygame.BLEND_RGB_ADD)
        
        if self.reverse:
            if self.radius >= 30:
                self.radius -= 30
            else:
                if(not self.didDamage):
                    self.doDamage = True
                else:
                    self.doDamage = False
                self.didDamage = True
                self.radius = 0
                screen.blit(self.draw_rect(1920, (self.alpha,self.alpha,self.alpha)), (0,0), special_flags = pygame.BLEND_RGB_ADD)
                if(self.alpha >= 5):
                    self.alpha -= 5
        else:
            if self.radius < self.maxRadius:
                self.radius += 20
            else: 
                self.reverse = True
        self.TTL -= 1
        projectileList.clear()
        return False

    def draw_particle(self, radius, color):
        surf = pygame.Surface((radius * 2, radius* 2))
        pygame.draw.circle(surf, color, (radius, radius), radius)
        surf.set_colorkey((0,0,0))
        return surf
    
    def draw_rect(self, size, color):
        surf = pygame.Surface((size, size))
        rect = pygame.Rect(0, 0, size, size)
        pygame.draw.rect(surf, color, rect)
        
        surf.set_colorkey((0,0,0))
        return surf