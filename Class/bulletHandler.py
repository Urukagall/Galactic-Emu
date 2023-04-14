import math
import pygame
from Class.projectile import Projectile

class BulletHandler():
    maxSpinSpeed=0
    radius=100
    bulletAcceleration=0
    bulletCurve=0
    invertSpin=False
    bulletTTL = 0

    def __init__(self, firingSpeed, arrayNumber, angleBetweenArrays):
        self.firingSpeed = firingSpeed
        self.arrayNumber = arrayNumber
        self.angleBetweenArrays = angleBetweenArrays
        self.arrayList = []
        arrayX = 100
        arrayY = 100
        for array in range(self.arrayNumber):
            array = (arrayX,arrayY)
            self.arrayList.append(array)
            arrayX = math.cos(self.angleBetweenArrays) - math.sin(self.angleBetweenArrays)
            arrayY = math.sin(self.angleBetweenArrays) + math.cos(self.angleBetweenArrays)
    
    def update(self):
        print("Update")
        #Import missile model
        missile = pygame.image.load("img/missile.png")
        missile = pygame.transform.scale(missile, (50, 50))
        missileWidth = missile.get_width()
        for array in self.arrayList:
            bullet = Projectile(array[0], array[1],missileWidth,missile)
        

