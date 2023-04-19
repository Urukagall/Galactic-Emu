from Class.bulletHandler import BulletHandler
from Pattern.enemiesPattern import bossPattern
import pygame, math

class Boss():
    def __init__(self,health, speed, x, y, size, displayWidth, displayHeight, score, image, projectileList, facing, enemyList):
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
            newBH.move(self.x, self.y)
            
        enemyList.append(self)
        print(enemyList)

    def move(self, veloX, veloY):
        self.x = self.x + veloX * self.speed
        self.y = self.y + veloY * self.speed
        for BH in self.BHList:
            BH.move(self.x, self.y)

    def takeDmg(self, dmg):
        self.health -= dmg
        if(self.health <= 0):
            #Die
            #enemyList.pop(enemyList.index(self))
            pass
    
    def update(self, player):
        #move
        bossPattern(self, 1)
        for BH in self.BHList:
            if BH > 0:
                offset = self.cooldowns[BH - 1]
            if self.cooldowns[BH] <= 0 - offset:
                direction = (0, 1)
                if BH[5]: #shoot toward player
                    radians = math.atan2(player.Y - self.y, player.X - self.x)
                    destX = math.cos(radians)
                    destY = math.sin(radians)
                    direction = (destX, destY)
                self.BHList[BH].update(direction)
                self.cooldowns[BH] = self.timeBetweenShots[BH]*60
            else:
                self.cooldowns[BH] -= 1
    
    def changePattern(self, patternNum):
        '''
        -- How to add a pattern --
        [timeBetweenShots, bulletSpeed, arrayNumber, angleBetweenArrays, image, shootTowardPlayer?, rotation]
        '''
        if patternNum == 1:
            BH1 = [1, 1, 4, 90, "bullet.png", False, 10]
            BH2 = [1, 1, 4, 90, "bullet.png", False, -10]
            self.BHdata.append(BH1)
            self.BHdata.append(BH2)
            self.timeBetweenShots.append(BH1[0])
            self.timeBetweenShots.append(BH2[0])
        elif patternNum == 2:
            BH1 = [5, 3, 10, "bigBall.png", True, 0]
            BH2 = [0.5, 4, 90, "bullet.png", False, 10]
            self.BHdata.append(BH1)
            self.BHdata.append(BH2)
            self.timeBetweenShots.append(BH1[0])
            self.timeBetweenShots.append(BH2[0])
        elif patternNum == 3:
            BH1 = [1, 1, 4, 90, "bullet.png", False, 10]
            BH2 = [1, 1, 4, 90, "bullet.png", False, -10]
            BH3 = [5, 3, 10, "bigBall.png", True, 0]
            self.BHdata.append(BH1)
            self.BHdata.append(BH2)
            self.BHdata.append(BH3)
            self.timeBetweenShots.append(BH1[0])
            self.timeBetweenShots.append(BH2[0])
            self.timeBetweenShots.append(BH3[0])