from Class.bulletHandler import BulletHandler
from Functions.enemiesPattern import bossPattern
import pygame, math

class Boss():
    def __init__(self,health, speed, x, y, size, displayWidth, displayHeight, score, image, projectileList, facing):

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

    def move(self, veloX, veloY):
        self.x = self.x + veloX * self.speed
        self.y = self.y + veloY * self.speed
        for BH in self.BHList:
            BH.move(self.x + self.size/2, self.y + 100)

    def takeDmg(self, dmg, enemyList, player):
        self.health -= dmg
        if(self.health <= 0):
            self.projectileList.clear()
            enemyList.pop(enemyList.index(self))
        elif self.health <= 3000:
            if self.patternNum != 5:
                self.patternNum = 5
                self.changePattern()
        elif self.health <= 5000:
            if self.patternNum != 4:
                self.patternNum = 4
                self.changePattern()
        elif self.health <= 7000:
            if self.patternNum != 3:
                self.patternNum = 3
                self.changePattern()
        elif self.health <= 8000:
            if self.patternNum != 2:
                self.patternNum = 2
                self.changePattern()
        
    
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

        '''Blue bullets import'''
        ballBlue = pygame.image.load("img/bullets/ball.png").convert_alpha()
        ballBlue = pygame.transform.scale(ballBlue, (ballBlue.get_width()*2, ballBlue.get_height()*2))
        bigBallBlue = pygame.image.load("img/bullets/bigBall.png").convert_alpha()
        bigBallBlue = pygame.transform.scale(bigBallBlue, (50, 50))
        bulletBlue =  pygame.image.load("img/bullets/bullet.png").convert_alpha()
        bulletBlue = pygame.transform.scale(bulletBlue, (bulletBlue.get_width()*2, bulletBlue.get_height()*2))
        carreauBlue =  pygame.image.load("img/bullets/carreau.png").convert_alpha()
        carreauBlue = pygame.transform.scale(carreauBlue, (carreauBlue.get_width()*2, carreauBlue.get_height()*2))
        missileBlue = pygame.image.load("img/bullets/missile.png").convert_alpha()
        missileBlue = pygame.transform.scale(missileBlue, (missileBlue.get_width(), missileBlue.get_height()))
        '''Red bullets import'''
        ballRed = pygame.image.load("img/bullets/ball_red.png").convert_alpha()
        ballRed = pygame.transform.scale(ballRed, (ballRed.get_width()*2, ballRed.get_height()*2))
        bigBallRed = pygame.image.load("img/bullets/bigBall_red.png").convert_alpha()
        bigBallRed = pygame.transform.scale(bigBallRed, (50, 50))
        bulletRed =  pygame.image.load("img/bullets/bullet_red.png").convert_alpha()
        bulletRed = pygame.transform.scale(bulletRed, (bulletRed.get_width()*2, bulletRed.get_height()*2))
        carreauRed =  pygame.image.load("img/bullets/carreau_red.png").convert_alpha()
        carreauRed = pygame.transform.scale(carreauRed, (carreauRed.get_width()*2, carreauRed.get_height()*2))
        missileRed = pygame.image.load("img/bullets/missile_red.png").convert_alpha()
        missileRed = pygame.transform.scale(missileRed, (missileRed.get_width(), missileRed.get_height()))
        '''Green bullets import'''
        ballGreen = pygame.image.load("img/bullets/ball_green.png").convert_alpha()
        ballGreen = pygame.transform.scale(ballGreen, (ballGreen.get_width()*2, ballGreen.get_height()*2))
        bigBallGreen = pygame.image.load("img/bullets/bigBall_green.png").convert_alpha()
        bigBallGreen = pygame.transform.scale(bigBallGreen, (50, 50))
        bulletGreen =  pygame.image.load("img/bullets/bullet_green.png").convert_alpha()
        bulletGreen = pygame.transform.scale(bulletGreen, (bulletGreen.get_width()*2, bulletGreen.get_height()*2))
        carreauGreen =  pygame.image.load("img/bullets/carreau_green.png").convert_alpha()
        carreauGreen = pygame.transform.scale(carreauGreen, (carreauGreen.get_width()*2, carreauGreen.get_height()*2))
        missileGreen = pygame.image.load("img/bullets/missile_green.png").convert_alpha()
        missileGreen = pygame.transform.scale(missileGreen, (missileGreen.get_width(), missileGreen.get_height()))
        '''Purple bullets import'''
        ballPurple = pygame.image.load("img/bullets/ball_purple.png").convert_alpha()
        ballPurple = pygame.transform.scale(ballPurple, (ballPurple.get_width()*2, ballPurple.get_height()*2))
        bigBallPurple = pygame.image.load("img/bullets/bigBall_purple.png").convert_alpha()
        bigBallPurple = pygame.transform.scale(bigBallPurple, (50, 50))
        bulletPurple =  pygame.image.load("img/bullets/bullet_purple.png").convert_alpha()
        bulletPurple = pygame.transform.scale(bulletPurple, (bulletPurple.get_width()*2, bulletPurple.get_height()*2))
        carreauPurple =  pygame.image.load("img/bullets/carreau_purple.png").convert_alpha()
        carreauPurple = pygame.transform.scale(carreauPurple, (carreauPurple.get_width()*2, carreauPurple.get_height()*2))
        missilePurple = pygame.image.load("img/bullets/missile_purple.png").convert_alpha()
        missilePurple = pygame.transform.scale(missilePurple, (missilePurple.get_width(), missilePurple.get_height()))

        '''
        -- How to add a pattern --
        [timeBetweenShots, bulletSpeed, arrayNumber, angleBetweenArrays, image, shootTowardPlayer?, rotation]
        '''

        self.BHdata.clear()
        self.BHList.clear()
        self.cooldowns.clear()
        self.timeBetweenShots.clear()
        if self.patternNum == 1:
            BH1 = [0.75, 2, 8, 45, carreauPurple, False, 3]
            BH2 = [0.75, 2, 8, 45, carreauGreen, False, -3]
            self.BHdata.append(BH1)
            self.BHdata.append(BH2)
            self.timeBetweenShots.append(BH1[0])
            self.timeBetweenShots.append(BH2[0])     
            self.projectileList.clear()     
        elif self.patternNum == 2:
            BH1 = [1, 2, 8, 45, carreauGreen, False, 3]
            BH2 = [1, 2, 8, 45, carreauPurple, False, -3]
            BH3 = [1, 3, 5, 15, bulletBlue, True, 0]
            self.BHdata.append(BH1)
            self.BHdata.append(BH2)
            self.BHdata.append(BH3)
            self.timeBetweenShots.append(BH1[0])
            self.timeBetweenShots.append(BH2[0])
            self.timeBetweenShots.append(BH3[0])
        elif self.patternNum == 3:
            BH1 = [0.5, 2, 8, 45, bulletBlue, False, -3]
            BH2 = [1, 8, 3, 10, bigBallRed, True, 0]
            self.BHdata.append(BH1)
            self.BHdata.append(BH2)
            self.timeBetweenShots.append(BH1[0])
            self.timeBetweenShots.append(BH2[0])
            self.projectileList.clear()
        elif self.patternNum == 4:
            BH1 = [0.5, 2, 8, 45, bulletGreen, False, -3]
            BH2 = [0.5, 8, 8, 10, bigBallPurple, False, -3]
            BH3 = [3, 15, 3, 10, carreauRed, True, 0]
            self.BHdata.append(BH1)
            self.BHdata.append(BH2)
            self.BHdata.append(BH3)
            self.timeBetweenShots.append(BH1[0])
            self.timeBetweenShots.append(BH2[0])
            self.timeBetweenShots.append(BH3[0])  
            self.projectileList.clear()
        elif self.patternNum == 5:
            BH1 = [0.5, 2, 8, 45, bulletPurple, True, -3]
            BH2 = [0.5, 5, 2, 10, bigBallBlue, True, 0]
            BH3 = [3, 1, 5, 20, carreauGreen, True, 0]
            BH4 = [3, 25, 1, 0, missileRed, True, 0]
            self.BHdata.append(BH1)
            self.BHdata.append(BH2)
            self.BHdata.append(BH3)
            self.BHdata.append(BH4)
            self.timeBetweenShots.append(BH1[0])
            self.timeBetweenShots.append(BH2[0])
            self.timeBetweenShots.append(BH3[0])
            self.timeBetweenShots.append(BH4[0])
            self.projectileList.clear()

        #create new bullet handlers
        for BH in self.BHdata:
            index = self.BHdata.index(BH)
            newBH = BulletHandler(BH[1], BH[2], BH[3], self.projectileList, BH[4], BH[6])
            self.cooldowns.append(self.timeBetweenShots[index])
            self.BHList.append(newBH)
            newBH.move(self.x, self.y)