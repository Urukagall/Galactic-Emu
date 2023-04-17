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

    def __init__(self, bulletSpeed, arrayNumber, angleBetweenArrays, projectileList, img, isHoming = False, isPlayer = False):
        self.bulletSpeed = bulletSpeed
        self.arrayNumber = arrayNumber
        self.angleBetweenArrays = angleBetweenArrays
        self.arrayList = []
        self.projectileList = projectileList
        self.img = img
        self.isPlayer = isPlayer
        self.isHoming = isHoming

        
    
    def update(self, direction):
        #Import bullet image
        bulletWidth = self.img.get_width()

        numNegatives = math.floor(self.arrayNumber / 2)
        numPositives = math.ceil(self.arrayNumber / 2)
        arrayMax = numPositives - 1
        arrayMin = -numNegatives

        for array in range(arrayMin, arrayMax+1):
            #create bullet
            directionAngle = math.atan2(direction[1], direction[0])

            radians = math.radians(array * self.angleBetweenArrays) + directionAngle
            destX = math.cos(radians)
            destY = math.sin(radians)
            arrayDirection = (destX, destY)
            bullet = Projectile(self.X, self.Y, bulletWidth, self.img, arrayDirection, 1, self.isHoming, 1920, 1080, self.projectileList, self.bulletSpeed, self.isPlayer)
            

        

    def move(self, targetX, targetY):
        '''Updates the position of the bullet handler'''
        self.X = targetX
        self.Y = targetY
