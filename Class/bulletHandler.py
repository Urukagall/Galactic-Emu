import math
import pygame
from Class.projectile import Projectile
class BulletHandler():
    maxSpinSpeed=0
    radius=100
    bulletAcceleration=0
    invertSpin=False
    bulletTTL = 0
    X = 0
    Y = 0

    def __init__(self, bulletSpeed, arrayNumber, angleBetweenArrays, projectileList, img, rotation=0,isHoming = False, isPlayer = False, damage = 1):
        self.bulletSpeed = bulletSpeed
        self.arrayNumber = arrayNumber
        self.angleBetweenArrays = angleBetweenArrays
        self.arrayList = []
        self.projectileList = projectileList
        self.img = img
        self.rotationIncrement = rotation
        self.isPlayer = isPlayer
        self.isHoming = isHoming
        self.rotation = rotation

        self.angleOffset = 0
        
    
    def update(self, direction):
        #Import bullet image
        bulletWidth = self.img.get_width()

        numNegatives = math.floor(self.arrayNumber / 2)
        numPositives = math.ceil(self.arrayNumber / 2)
        arrayMax = numPositives - 1
        arrayMin = -numNegatives
        
        if abs(arrayMin) != arrayMax:
            #nombre pair
            self.angleOffset = self.angleBetweenArrays /2

        for array in range(arrayMin, arrayMax+1):
            #create bullet
            directionAngle = math.atan2(direction[1], direction[0])

            radians = math.radians(array * self.angleBetweenArrays + self.rotation + self.angleOffset) + directionAngle
            destX = math.cos(radians)
            destY = math.sin(radians)
            arrayDirection = (destX, destY)
            bullet = Projectile(self.X, self.Y, bulletWidth, self.img, arrayDirection, 1, self.isHoming, 1920, 1080, self.bulletSpeed, self.isPlayer)
            self.projectileList.append(bullet)
            self.rotation += self.rotationIncrement
        

    def move(self, targetX, targetY):
        '''Updates the position of the bullet handler'''
        self.X = targetX
        self.Y = targetY
