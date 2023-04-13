# Init
print("Hello Today I'm Gonna Teach You")
import pygame
import math
import pygame.time
pygame.init()
clock = pygame.time.Clock()

# Create Window
displayHeight = 1080
displayWidth = 1920
backgroundColor = (200,200,200)
screen = pygame.display.set_mode((displayWidth, displayHeight))
pygame.display.set_caption("Endless Scroll")



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
            
#Creating the player
player = Player(10, 5, 100, pygame.image.load("img/emeu.jpg").convert())

bg = pygame.image.load("img/back.png").convert()
bg = pygame.transform.scale(bg, (1920, 1080))
bg_height = bg.get_height()

scroll = 0 
tiles = math.ceil(displayHeight / bg_height) + 1



# Main Loop
running = True
while running:
    # run the game at a constant 60fps
    clock.tick(60)
    #Did the user clicked the close button ?
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            running=False
        elif events.type == pygame.KEYDOWN:
            if events.key == pygame.K_ESCAPE:
                running=False
    
    #draw scrolling background 
    for i in range(0, tiles):
      screen.blit(bg,(0, (-1 * i) * bg_height - scroll))

    #scroll background
    scroll -= 5

    #reset scroll
    if abs (scroll) > bg_height:
        scroll = 0

    pressed = pygame.key.get_pressed()

    if pressed[pygame.K_LSHIFT]:
        player.speed = player.slowSpeed
    else: 
        player.speed = player.basicSpeed

    #PLAYER 1 Y
    if pressed[pygame.K_z]:
        player.move(0,-1)
    elif pressed[pygame.K_s]:
        player.move(0,1)
    else :
        playerYVelocity = 0
    # PLAYER 1 X
    if pressed[pygame.K_d]:
        player.move(1,0)
    elif pressed[pygame.K_q]:
        player.move(-1,0)
    else :
        playerXVelocity = 0

    

    #Draw 
    #P1
    screen.blit(player.img, (player.X, player.Y))
    pygame.display.update()
pygame.quit()
