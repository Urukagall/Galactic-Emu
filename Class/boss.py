from Class.bulletHandler import BulletHandler
from Pattern.enemiesPattern import bossPattern
import pygame, math

class Boss():
    def __init__(self,health, speed, x, y, size, displayWidth, displayHeight, score, image, projectileList, facing):
        
        self.carreau_green = pygame.image.load("img/carreau_green.png")
        self.carreau_green = pygame.transform.scale(self.carreau_green, (self.carreau_green.get_width()*2, self.carreau_green.get_height()*2))

        self.carreau_purple = pygame.image.load("img/carreau_purple.png")
        self.carreau_purple = pygame.transform.scale(self.carreau_purple, (self.carreau_purple.get_width()*2, self.carreau_purple.get_height()*2))

        self.bigBall = pygame.image.load("img/bigBall.png")
        self.bullet = pygame.image.load("img/bullet.png")
        self.bullet = pygame.transform.scale(self.bullet, (self.bullet.get_width()*2, self.bullet.get_height()*2))

        self.health = health
        self.size = size
        self.displayWidth = displayWidth
        self.displayHeight = displayHeight
        self.score = score
        self.image = image
        #movement
        self.speed = speed
        self.x = x
        self.y = y
        self.facing = facing
        self.patternStep = 0
        #attack
        self.cooldowns = []
        self.timeBetweenShots = []
        self.BHdata = []
        self.BHList = []
        self.changePattern(1)


        for BH in self.BHdata:
            index = self.BHdata.index(BH)
            newBH = BulletHandler(BH[1], BH[2], BH[3], projectileList, BH[4], BH[6])
            self.cooldowns.append(self.timeBetweenShots[index])
            self.BHList.append(newBH)
            newBH.move(self.x, self.y)

    def move(self, veloX, veloY):
        self.x = self.x + veloX * self.speed
        self.y = self.y + veloY * self.speed
        for BH in self.BHList:
            BH.move(self.x + self.size/2, self.y + self.size/2)

    def takeDmg(self, dmg, enemyList):
        self.health -= dmg
        if(self.health <= 0):
            enemyList.pop(enemyList.index(self))
    
    def update(self, player):
        #move
        bossPattern(self, 1)
        for bulletHandler in self.BHList:
            index = self.BHList.index(bulletHandler)
            if index > 0:
                offset = self.cooldowns[index - 1]
            else:
                offset = 0

            if self.cooldowns[index] <= 0 - offset:
                direction = (0, 1)
                
                if self.BHdata[index][5] == True: #shoot toward player
                    radians = math.atan2(player.Y - self.y, player.X - self.x)
                    destX = math.cos(radians)
                    destY = math.sin(radians)
                    direction = (destX, destY)
                bulletHandler.update(direction)
                self.cooldowns[index] = self.timeBetweenShots[index]*60
            else:
                self.cooldowns[index] -= 1
    
    def changePattern(self, patternNum):
        '''
        -- How to add a pattern --
        [timeBetweenShots, bulletSpeed, arrayNumber, angleBetweenArrays, image, shootTowardPlayer?, rotation]
        '''
        if patternNum == 1:
            BH1 = [1, 2, 8, 45, self.carreau_purple, False, 3]
            self.BHdata.append(BH1)
            self.timeBetweenShots.append(BH1[0])
            BH2 = [1, 2, 8, 45, self.carreau_green, False, -3]
            self.BHdata.append(BH2)
            self.timeBetweenShots.append(BH2[0])
        elif patternNum == 2:
            BH1 = [5, 3, 10, self.bigBall, True, 0]
            BH2 = [0.5, 4, 90, self.bullet, False, 10]
            self.BHdata.append(BH1)
            self.BHdata.append(BH2)
            self.timeBetweenShots.append(BH1[0])
            self.timeBetweenShots.append(BH2[0])
        elif patternNum == 3:
            BH1 = [1, 1, 4, 90, self.bullet, False, 10]
            BH2 = [1, 1, 4, 90, self.bullet, False, -10]
            BH3 = [5, 3, 10, self.bigBall, True, 0]
            self.BHdata.append(BH1)
            self.BHdata.append(BH2)
            self.BHdata.append(BH3)
            self.timeBetweenShots.append(BH1[0])
            self.timeBetweenShots.append(BH2[0])
            self.timeBetweenShots.append(BH3[0])