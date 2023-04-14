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
        classicBullet = pygame.image.load("img/bullet.png")
        classicBullet = pygame.transform.scale(classicBullet, (50, 50))
        classicBulletWidth = classicBullet.get_width()
        for array in self.arrayList:
            # j'ai mis d'autre argument parceque j'ai changer les bullet et il faudra changer le 1920 et 1080 après
            bullet = Projectile(array[0], array[1],classicBulletWidth, classicBullet, 10, 5, False, 1920, 1080)
        

