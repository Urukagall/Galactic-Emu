import math

class Projectile():

    def __init__(self, x, y, width, image, velocity, damage, isHoming, displayWidth, displayHeight):
        self.x = x
        self.y = y
        self.width = width
        self.image = image
        self.velocity = velocity
        self.damage = damage
        self.isHoming = isHoming
        self.displayWidth = displayWidth
        self.displayHeight = displayHeight
        
    def move(self, velox, veloy):
        self.x = self.x + velox * self.velocity
        self.y = self.y + veloy * self.velocity
