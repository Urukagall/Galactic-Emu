import math

class Projectile():
    def __init__(self, x, y, width, image, velocity, damage, isHoming, displayWidth, displayHeight, projectileList, player=False):
        self.player = player
        self.x = x
        self.y = y
        self.width = width
        self.image = image
        self.velocity = velocity
        self.damage = damage
        self.isHoming = isHoming
        self.displayWidth = displayWidth
        self.displayHeight = displayHeight
        projectileList.append(self)
        
    def update(self):
        self.x = self.x + self.velocity[0]
        self.y = self.y + self.velocity[1]

        '''The bullet is destroyed when exiting the screen'''
        if self.x < 0 - self.width:
            del(self)
        elif self.x > self.displayWidth + self.width:
            del(self)
        if self.y < 0 - self.width:
            del(self)
        elif self.y > self.displayHeight + self.width:
            del(self)