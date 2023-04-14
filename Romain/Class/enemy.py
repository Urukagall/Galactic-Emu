class Enemy():
    
    def __init__(self,health, speed, x, y, size, displayWidth, displayHeight, score, image):
        self.health = health
        self.speed = speed
        self.x = x
        self.y = y
        self.size = size
        self.displayWidth = displayWidth
        self.displayHeight = displayHeight
        self.score = score
        self.image = image

    def move(self, veloX, veloY):
        self.x = self.x + veloX * self.speed
        self.y = self.y + veloY * self.speed

    def takeDmg(self, dmg):
        self.health -= dmg

    def movementPattern(self, func):
        self.x = func(self.x, self.speed)