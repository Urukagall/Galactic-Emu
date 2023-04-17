from Class.bulletHandler import BulletHandler
from Pattern.enemiesPattern import firstPattern
import pygame, math

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

    def takeDmg(self, dmg, enemyList):
        self.health -= dmg
        if(self.health <= 0):
            enemyList.pop(enemyList.index(self))
    
    def update(self, player=None):
        #move
        firstPattern(self)
        if self.cooldown <= 0:
            #shoot
            direction = (0, 1)
            if player:
                radians = math.atan2(player.Y - self.y, player.X - self.x)

                destX = math.cos(radians)
                destY = math.sin(radians)
                direction = (destX, destY)
            
            self.bulletHandler.update(direction)
            self.cooldown = self.timeBetweenShots*60
        else:
            self.cooldown -= 1