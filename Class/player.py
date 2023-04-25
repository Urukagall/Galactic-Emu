import math
import pygame
from Class.bulletHandler import BulletHandler
from Class.particle import Particle
from Functions.jsonReader import *
from Functions.darken import darken

class Player():
    def __init__(self, basicSpeed, slowSpeed, size, displayWidth, displayHeight, dashSpeed,cooldownDash,timeDash, lives, projectileList, imgBullet, imgMissile, imgPrecise, img, imgShield):
        self.X = 800
        self.Y = 500
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
        self.img = img
        self.imgShield = imgShield
        self.money = 0
        self.timeInvincible = 3
        self.dashInvulnerability = 0
        self.secondaryWeapon1 = get("save.json", "secondaryWeapon1")
        self.secondaryWeapon2 = get("save.json", "secondaryWeapon2")

        # Bullet Stats
        self.bulletImg = imgBullet
        self.bulletSpeed = 10
        self.arrayNumber = 1
        self.angleBetweenArrays = 10
        self.bulletDamage = 1
        self.timeBetweenShots = 10  #60 = 1sec
        self.cooldown = self.timeBetweenShots
        
        # Missile Stats
        self.missileImg = imgMissile
        self.missileSpeed = 10
        self.missileArrayNumber = 1
        self.angleBetweenMissileArrays = 30
        self.missileDamage = 1
        self.timeBetweenMissiles = 20  #60 = 1sec
        self.missileCooldown = self.timeBetweenMissiles

        # Ultimate Stats
        self.timeBetweenUltimates = 1200
        self.ultimateDmg = 50
        self.ultimateCooldown = self.timeBetweenUltimates

        #Secondary weapons
        self.ballBlue = pygame.image.load("img/bullets/ball.png").convert_alpha()
        self.ballBlue = pygame.transform.scale(self.ballBlue, (self.ballBlue.get_width(), self.ballBlue.get_height()))
        self.ballBlue = darken(self.ballBlue).convert_alpha()
        self.spiralImg = darken(self.bulletImg, 49).convert_alpha()
        self.aim54 = pygame.image.load("img/bullets/aim54.png").convert_alpha()
        self.aim54 = pygame.transform.scale(self.aim54, (self.aim54.get_width()*2, self.aim54.get_height()*2))
        self.aim54 = darken(self.aim54).convert_alpha()
        self.timeBewteenAutocanonShots = 1
        self.autocanonCooldown = self.timeBewteenAutocanonShots
        self.timeBewteenShotgunShots = 60
        self.shotgunCooldown = self.timeBewteenShotgunShots
        self.timeBewteenPhoenixShots = self.timeBetweenMissiles * 5
        self.phoenixCooldown = self.timeBewteenPhoenixShots

        self.preciseImg = imgPrecise


        self.projectileList = projectileList

        self.bulletHandler = BulletHandler(self.bulletSpeed, self.arrayNumber, self.angleBetweenArrays, self.projectileList, self.bulletImg, isHoming=False,isPlayer = True,damage=self.bulletDamage)
        self.missileHandler = BulletHandler(self.missileSpeed, self.missileArrayNumber, self.angleBetweenMissileArrays, self.projectileList, self.missileImg, isHoming=True,isPlayer = True,damage=self.missileDamage)
        self.preciseHandler = BulletHandler(self.bulletSpeed, self.arrayNumber+1, self.angleBetweenArrays/2, self.projectileList, self.preciseImg, isHoming=False, isPlayer=True)
        #secondary (optionnal) weapons
        self.autocanonHandler = BulletHandler(self.bulletSpeed, 1, 0, self.projectileList, self.ballBlue, 0, False, True, self.bulletDamage)
        self.shotgunHandler = BulletHandler(self.bulletSpeed, 5, 10, self.projectileList, self.ballBlue, 0, False, True, self.bulletDamage)
        self.spiralHandler = BulletHandler(self.bulletSpeed, self.arrayNumber*2, 360/(self.arrayNumber), self.projectileList, self.spiralImg, 5, False, True, self.bulletDamage)
        self.phoenixHandler = BulletHandler(self.missileSpeed*2, 1, 0, self.projectileList, self.aim54, 0, True, True, self.missileDamage*20)


    def redefined(self):
        self.bulletHandler = BulletHandler(self.bulletSpeed, self.arrayNumber, self.angleBetweenArrays, self.projectileList, self.bulletImg, isHoming=False,isPlayer = True,damage=self.bulletDamage)
        self.missileHandler = BulletHandler(self.missileSpeed, self.missileArrayNumber, self.angleBetweenMissileArrays, self.projectileList, self.missileImg, isHoming=True,isPlayer = True,damage=self.missileDamage)
        self.preciseHandler = BulletHandler(self.bulletSpeed, self.arrayNumber+1, self.angleBetweenArrays/2, self.projectileList, self.preciseImg, isHoming=False, isPlayer=True)
        #secondary (optionnal) weapons
        self.autocanonHandler = BulletHandler(self.bulletSpeed, 1, 0, self.projectileList, self.ballBlue, 0, False, True, self.bulletDamage)
        self.shotgunHandler = BulletHandler(self.bulletSpeed, 10, 5, self.projectileList, self.ballBlue, 0, False, True, self.bulletDamage)
        self.phoenixHandler = BulletHandler(self.missileSpeed*2, 1, 0, self.projectileList, self.aim54, 0, True, True, self.missileDamage*20)
        self.spiralHandler = BulletHandler(self.bulletSpeed, self.arrayNumber, 360/(self.arrayNumber), self.projectileList, self.spiralImg, 5, False, True, self.bulletDamage)

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
        #move the bulletHandlers to the center of the player sprite
        self.bulletHandler.move(self.X+self.size/4, self.Y+self.size/4)
        self.missileHandler.move(self.X+self.size/4, self.Y+self.size/4)
        self.preciseHandler.move(self.X+self.size/4, self.Y+self.size/4)
        if self.secondaryWeapon1 == "autocanon":
            self.autocanonHandler.move(self.X, self.Y+self.size/2)
        elif self.secondaryWeapon1 == "spiral":
            self.spiralHandler.move(self.X, self.Y+self.size/2)

        if self.secondaryWeapon2 == "shotgun":
            self.shotgunHandler.move(self.X+self.size, self.Y+self.size/2)
        elif self.secondaryWeapon2 == "phoenix":
            self.phoenixHandler.move(self.X+self.size, self.Y+self.size/2)
    
    def getHit(self):
        if self.lives > 0:
            self.lives -= 1
        else:
            print("You lost")
        
    def updateMoney(self,gain):
        self.money += gain
    
    def shoot(self, shift):
        direction = (0,-1)
        if shift:
            self.preciseHandler.update(direction)
        self.bulletHandler.update(direction)
        if self.secondaryWeapon1 == "spiral":
            self.spiralHandler.update(direction)

    def updateSecondaries(self):
        direction = (0, -1)
        if self.secondaryWeapon1 == "autocanon":
            if self.autocanonCooldown <= 0:
                self.autocanonCooldown = self.timeBewteenAutocanonShots
                self.autocanonHandler.update(direction)
            else:
                self.autocanonCooldown -= 1

        if self.secondaryWeapon2 == "shotgun":
            if self.shotgunCooldown <= 0:
                self.shotgunCooldown = self.timeBewteenShotgunShots
                self.shotgunHandler.update(direction)
            else:
                self.shotgunCooldown -= 1
        elif self.secondaryWeapon2 == "phoenix":
            if self.phoenixCooldown <= 0:
                self.phoenixCooldown = self.timeBewteenPhoenixShots
                self.phoenixHandler.update(direction)
            else:
                self.phoenixCooldown -= 1

    def shootHoming(self):
        direction = (0,-1)
        self.missileHandler.update(direction)
    
    def shootUltimate(self, particleList):
        ultimateSize = 100
        particleColor = pygame.Color(255,255,255)
        particleCoordinates = pygame.math.Vector2(self.displayWidth/2, self.displayHeight/2)
        particle = Particle(particleCoordinates, ultimateSize, particleColor, particleList)