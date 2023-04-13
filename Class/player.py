class Player:
    X = 0
    Y = 0
    def __init__(self, basicSpeed, slowSpeed, size, img):
        self.basicSpeed = basicSpeed
        self.slowSpeed = slowSpeed
        self.speed = basicSpeed
        self.size = size
        self.img = pygame.transform.scale(img, (self.size, self.size))

    def move(self, veloX, veloY):
        if veloX != 0 and veloY != 0:
            self.X = self.X + math.sqrt(1/2) * self.speed
            self.Y = self.Y + math.sqrt(1/2) * self.speed
        else:
            self.X = self.X + veloX * self.speed
            self.Y = self.Y + veloY * self.speed
        
        #Stop player from going out of the screen
        if self.X > displayWidth - self.size:
            self.X = displayWidth - self.size
        if self.X < 0:
            self.X = 0
        if self.Y > displayHeight - self.size:
            self.Y = displayHeight - self.size
        if self.Y < 0:
            self.Y = 0
