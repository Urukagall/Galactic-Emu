from Class.bulletHandler import BulletHandler
from Functions.enemiesPattern import bossPattern
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
        self.patternNum = 1
        
        self.projectileList = projectileList
        self.changePattern()

        '''for BH in self.BHdata:
            index = self.BHdata.index(BH)
            newBH = BulletHandler(BH[1], BH[2], BH[3], self.projectileList, BH[4], BH[6])
            self.cooldowns.append(self.timeBetweenShots[index])
            self.BHList.append(newBH)
            newBH.move(self.x, self.y)'''

    def move(self, veloX, veloY):
        self.x = self.x + veloX * self.speed
        self.y = self.y + veloY * self.speed
        for BH in self.BHList:
            BH.move(self.x + self.size/2, self.y + 100)

    def takeDmg(self, dmg, enemyList):
        self.health -= dmg
        if(self.health <= 0):
            enemyList.pop(enemyList.index(self))
        elif self.health <= 3000:
            if self.patternNum != 3:
                self.patternNum =3
                self.changePattern()
                print("Patern 3")
        elif self.health <= 6000:
            if self.patternNum != 2:
                self.patternNum =2
                self.changePattern()
                print("Patern 2")
        
    
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
                    playerHitbox = pygame.Rect(0,0, player.size/8, player.size/8)
                    # center the hitbox on the ship's cockpit
                    target = pygame.math.Vector2(player.X+player.size/2 - playerHitbox.width/4, player.Y+player.size/4)
                    radians = math.atan2(target.y - bulletHandler.Y, target.x - bulletHandler.X)
                    destX = math.cos(radians)
                    destY = math.sin(radians)
                    direction = (destX, destY)
                bulletHandler.update(direction)
                self.cooldowns[index] = self.timeBetweenShots[index]*60
            else:
                self.cooldowns[index] -= 1
    
    def changePattern(self):
        '''
        -- How to add a pattern --
        [timeBetweenShots, bulletSpeed, arrayNumber, angleBetweenArrays, image, shootTowardPlayer?, rotation]
        '''

        self.BHdata.clear()
        self.BHList.clear()
        self.cooldowns.clear()
        self.timeBetweenShots.clear()
        if self.patternNum == 1:
            BH1 = [0.5, 2, 8, 45, self.carreau_purple, False, 3]
            BH2 = [0.5, 2, 8, 45, self.carreau_green, False, -3]
            self.BHdata.append(BH1)
            self.BHdata.append(BH2)
            self.timeBetweenShots.append(BH1[0])
            self.timeBetweenShots.append(BH2[0])
        elif self.patternNum == 2:
            BH1 = [0.5, 2, 8, 45, self.bullet, False, -3]
            BH2 = [1, 8, 3, 10, self.bigBall, True, 0]
            self.BHdata.append(BH1)
            self.BHdata.append(BH2)
            self.timeBetweenShots.append(BH1[0])
            self.timeBetweenShots.append(BH2[0])
        elif self.patternNum == 3:
            BH1 = [1, 1, 8, 45, self.carreau_green, False, 3]
            BH2 = [1, 1, 8, 45, self.carreau_purple, False, -3]
            BH3 = [1, 3, 5, 15, self.bullet, True, 0]
            self.BHdata.append(BH1)
            self.BHdata.append(BH2)
            self.BHdata.append(BH3)
            self.timeBetweenShots.append(BH1[0])
            self.timeBetweenShots.append(BH2[0])
            self.timeBetweenShots.append(BH3[0])

        #create new bullet handlers
        for BH in self.BHdata:
            index = self.BHdata.index(BH)
            newBH = BulletHandler(BH[1], BH[2], BH[3], self.projectileList, BH[4], BH[6])
            self.cooldowns.append(self.timeBetweenShots[index])
            self.BHList.append(newBH)
            newBH.move(self.x, self.y)