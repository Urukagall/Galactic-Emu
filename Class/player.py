import math
import pygame
from Class.bulletHandler import BulletHandler
class Player():
    def __init__(self, basicSpeed, slowSpeed, size, displayWidth, displayHeight, dashSpeed,cooldownDash,timeDash, lives, projectileList):
        self.X = 0
        self.Y = 0
        self.basicSpeed = basicSpeed
        self.slowSpeed = slowSpeed
        self.speed = basicSpeed
        self.size = size
        self.displayWidth = displayWidth
        self.displayHeight = displayHeight
        self.dashSpeed = dashSpeed
        self.cooldownDash = cooldownDash
        self.timeDash = timeDash
        self.lives = lives

        self.projectileList = projectileList
        self.arrayNumber = 3
        self.bulletSpeed = 50
        self.angleBetweenArrays = 10
        self.timeBetweenShots = 0.3
        self.cooldown = self.timeBetweenShots
        self.timeBetweenMissiles = 10
        self.missileCooldown = self.timeBetweenMissiles
        self.timeBetweenUltimates = 20000
        self.ultimateCooldown = self.timeBetweenUltimates

        self.bulletImg = pygame.image.load("img/bullet.png")
        self.bulletImg = pygame.transform.scale(self.bulletImg, (50, 50))
        self.missileImg = pygame.image.load("img/missile.png")
        self.missileImg = pygame.transform.scale(self.missileImg, (50, 50))
        self.ultimateImg = pygame.image.load("img/grosse_boule.png")
        self.ultimateImg = pygame.transform.scale(self.ultimateImg, (50, 50))

        self.bulletHandler = BulletHandler(self.bulletSpeed, self.arrayNumber, self.angleBetweenArrays, self.projectileList, self.bulletImg, isHoming=False,isPlayer = True)
        self.missileHandler = BulletHandler(self.bulletSpeed, self.arrayNumber, self.angleBetweenArrays, self.projectileList, self.missileImg, isHoming=True,isPlayer = True)
        self.ultimateHandler = BulletHandler(self.bulletSpeed, self.arrayNumber, self.angleBetweenArrays, self.projectileList, self.ultimateImg, isHoming=False, isPlayer=True)

    def move(self, veloX, veloY):
        if veloX != 0 and veloY != 0:
            self.X = self.X + math.sqrt(1/2) * self.speed * veloX
            self.Y = self.Y + math.sqrt(1/2) * self.speed * veloY
        else:
            self.X = self.X + veloX * self.speed
            self.Y = self.Y + veloY * self.speed
        
        #Stop player from going out of the screen
        if self.X > self.displayWidth - self.size:
            self.X = self.displayWidth - self.size
        if self.X < 0:
            self.X = 0
        if self.Y > self.displayHeight - self.size:
            self.Y = self.displayHeight - self.size
        if self.Y < 0:
            self.Y = 0
        self.bulletHandler.move(self.X, self.Y)
        self.missileHandler.move(self.X, self.Y)
    
    def getHit(self):
        if self.lives > 0:
            self.lives -= 1
        else:
            print("You lost")
        

    def shoot(self):
        self.bulletHandler.update()

    def shootHoming(self):
        self.missileHandler.update()
