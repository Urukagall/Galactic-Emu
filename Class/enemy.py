class Enemy:
    def __init__(self, x, y):
        self.health = 50
        self.x = x
        self.y = y
        self.width = 150
        self.height = 150

    def takeDmg(self, dmg):
        self.health -= dmg