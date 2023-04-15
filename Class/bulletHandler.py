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

    def __init__(self, firingSpeed, arrayNumber, angleBetweenArrays, projectileList, img, isHoming = False, isPlayer = False):
        self.firingSpeed = firingSpeed
        self.arrayNumber = arrayNumber
        self.angleBetweenArrays = angleBetweenArrays
        self.arrayList = []
        self.projectileList = projectileList
        self.img = img
        self.isPlayer = isPlayer
        self.isHoming = isHoming

    
    def update(self):
        #Import bullet image
        bulletWidth = self.img.get_width()
        #create bullet
        if self.isPlayer:
            velocity = pygame.math.Vector2(0,-50)
        else:
            velocity = pygame.math.Vector2(0,10)
        bullet = Projectile(self.X, self.Y+10, bulletWidth, self.img, velocity, 5, self.isHoming, 1920, 1080, self.projectileList, self.isPlayer)

    def move(self, targetX, targetY):
        '''Updates the position of the bullet handler'''
        self.X = targetX
        self.Y = targetY