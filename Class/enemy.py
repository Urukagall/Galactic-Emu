class Enemy:
    def __init__(self,health, speed, x, y, size, displayWidth, displayHeight):
        self.health = health
        self.speed = speed
        self.x = x
        self.y = y
        self.size = size
        self.displayWidth = displayWidth
        self.displayHeight = displayHeight

    def move(self, velox, veloy):
        self.x = self.x + velox * self.speed
        self.y = self.y + veloy * self.speed

    def takeDmg(self, dmg):
        self.health -= dmg