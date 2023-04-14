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
    X = 0
    Y = 0

    def __init__(self, firingSpeed, arrayNumber, angleBetweenArrays, projectileList):
        self.firingSpeed = firingSpeed
        self.arrayNumber = arrayNumber
        self.angleBetweenArrays = angleBetweenArrays
        self.arrayList = []
        self.projectileList = projectileList

    
    def update(self):
        #Import missile model
        classicBullet = pygame.image.load("img/grosse_boule.png")
        classicBullet = pygame.transform.scale(classicBullet, (50, 50))
        classicBulletWidth = classicBullet.get_width()
        bullet = Projectile(self.X, self.Y+10, classicBulletWidth, classicBullet, (0,10), 5, False, 1920, 1080, self.projectileList)

    def move(self, targetX, targetY):
        self.X = targetX
        self.Y = targetY
        print("Moved to ("+str(self.X)+","+str(self.Y)+")")