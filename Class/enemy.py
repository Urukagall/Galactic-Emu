from Class.bulletHandler import BulletHandler

class Enemy():
    def __init__(self,health, speed, x, y, size, displayWidth, displayHeight, score, image, firingSpeed, arrayNumber, angleBetweenArrays, projectileList, timeBetweenShots):
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
        self.bulletHandler = BulletHandler(firingSpeed, arrayNumber, angleBetweenArrays, projectileList)
        self.bulletHandler.move(self.x, self.y)

    def move(self, veloX, veloY):
        self.x = self.x + veloX * self.speed
        self.y = self.y + veloY * self.speed
        self.bulletHandler.move(self.x, self.y)

    def takeDmg(self, dmg):
        self.health -= dmg
    
    def update(self):
        #shoot
        if self.cooldown == 0:
            self.bulletHandler.update()
            self.cooldown = self.timeBetweenShots*60
        else:
            self.cooldown -= 1
