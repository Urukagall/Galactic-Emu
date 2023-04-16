from Class.bulletHandler import BulletHandler
from Pattern.enemiesPattern import firstPattern
import pygame

class Enemy():
    def __init__(self,health, speed, x, y, size, displayWidth, displayHeight, score, image, firingSpeed, arrayNumber, angleBetweenArrays, projectileList, timeBetweenShots, facing):
        self.health = health
        self.speed = speed
        self.x = x
        self.y = y
        self.size = size
        self.displayWidth = displayWidth
        self.displayHeight = displayHeight
        self.score = score
        self.image = image
        self.timeBetweenShots = timeBetweenShots
        self.cooldown = self.timeBetweenShots
        self.facing = facing
        self.patternStep = 0

        self.bulletImg = pygame.image.load("img/grosse_boule.png")
        self.bulletImg = pygame.transform.scale(self.bulletImg, (50, 50))
        self.bulletHandler = BulletHandler(firingSpeed, arrayNumber, angleBetweenArrays, projectileList, self.bulletImg)
        self.bulletHandler.move(self.x, self.y)

    def move(self, veloX, veloY):
        self.x = self.x + veloX * self.speed
        self.y = self.y + veloY * self.speed
        self.bulletHandler.move(self.x, self.y)

    def takeDmg(self, dmg):
        self.health -= dmg
    
    def update(self):
        #shoot
        firstPattern(self)
        if self.cooldown <= 0:
            self.bulletHandler.update()
            self.cooldown = self.timeBetweenShots*60
        else:
            self.cooldown -= 1