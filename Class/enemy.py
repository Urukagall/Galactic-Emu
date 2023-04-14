from Class.bulletHandler import BulletHandler

class Enemy():
    def __init__(self,health, speed, x, y, size, displayWidth, displayHeight, score, image, firingSpeed, arrayNumber, angleBetweenArrays):
        self.health = health
        self.speed = speed
        self.x = x
        self.y = y
        self.size = size
        self.displayWidth = displayWidth
        self.displayHeight = displayHeight
        self.score = score
        self.image = image
        self.bulletHandler = BulletHandler(firingSpeed, arrayNumber, angleBetweenArrays)

    def move(self, veloX, veloY):
        self.x = self.x + veloX * self.speed
        self.y = self.y + veloY * self.speed

    def takeDmg(self, dmg):
        self.health -= dmg
    
    def shoot(self):
        print("Shoot")
        self.bulletHandler.update()
