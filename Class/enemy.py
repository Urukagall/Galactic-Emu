from Class.bulletHandler import BulletHandler
from Functions.enemiesPattern import firstPattern
import pygame, math

class Enemy():

    def __init__(self,aimAtPlayer,health, speed, x, y, size, displayWidth, displayHeight, score, image, bulletImg1, bulletSpeed, arrayNumber, angleBetweenArrays, projectileList, timeBetweenShots, facing, money = 10, bulletRotation=0, bulletSpeed2 = 0, arrayNumber2 = 0, angleBetweenArrays2 = 0, timeBetweenShots2=0, bulletImg2=[], aimAtPlayer2=True, bulletRotation2 = 0,  pattern=firstPattern):
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
        self.timeBetweenShots2 = timeBetweenShots2
        self.cooldown = self.timeBetweenShots
        self.cooldown2 = self.timeBetweenShots2

        self.aimAtPlayer = aimAtPlayer
        self.aimtAtPlayer2 = aimAtPlayer2
        self.facing = facing
        self.pattern = pattern
        self.patternStep = 0
        self.bulletImg1 = bulletImg1
        self.BHList = []
        
        self.money = money

        self.bulletRotation = bulletRotation
        self.bulletRotation2 = bulletRotation2
            
        self.bulletHandler = BulletHandler(bulletSpeed, arrayNumber, angleBetweenArrays, projectileList, self.bulletImg1, self.bulletRotation)
        self.BHList.append(self.bulletHandler)
        
        if bulletSpeed2 != 0:
            self.anotherBH = True
            self.bulletHandler2 = BulletHandler(bulletSpeed2, arrayNumber2, angleBetweenArrays2, projectileList, bulletImg2, self.bulletRotation2)
            self.bulletHandler2.move(self.x, self.y)
            self.BHList.append(self.bulletHandler2)
            
        for bulletHandler in self.BHList:
            bulletHandler.move(self.x, self.y)
        
        
    def move(self, veloX, veloY):
        self.x = self.x + veloX * self.speed
        self.y = self.y + veloY * self.speed
        for bulletHandler in self.BHList:   
            bulletHandler.move(self.x + self.size/2, self.y + self.size/2)

    def takeDmg(self, dmg, enemyList, player):
        self.health -= dmg
        if(self.health <= 0):
            enemyList.pop(enemyList.index(self))
            player.money += self.money
    
    def update(self, player):
        #move
        self.pattern(self)
        if self.cooldown <= 0:
            #shoot
            direction = (0, 1)
            if self.aimAtPlayer:
                playerHitbox = pygame.Rect(0,0, player.size/8, player.size/8)
                # center the hitbox on the ship's cockpit
                target = pygame.math.Vector2(player.X+player.size/2 - playerHitbox.width/4, player.Y+player.size/4)
                radians = math.atan2(target.y - self.y, target.x - self.x)
                destX = math.cos(radians)
                destY = math.sin(radians)
                direction = (destX, destY)
            self.BHList[0].update(direction)
            
            self.cooldown = self.timeBetweenShots*60
        else:
            self.cooldown -= 1

        if self.cooldown2 <= 0 - self.cooldown/2 and len(self.BHList) > 1:
            #shoot
            direction = (0, 1)
            if self.aimtAtPlayer2:
                radians = math.atan2(player.Y - self.y, player.X - self.x)
                destX = math.cos(radians)
                destY = math.sin(radians)
                direction = (destX, destY)
            self.BHList[1].update(direction)
            
            self.cooldown2 = self.timeBetweenShots2*60
        else:
            self.cooldown2 -= 1