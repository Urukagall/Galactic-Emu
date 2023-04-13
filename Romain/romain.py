# Init
print("Hello Today I'm Gonna Teach You")
import pygame
import math
import pygame.time
pygame.init()
clock = pygame.time.Clock()

class Enemy:
    def __init__(self, x, y):
        self.health = 50
        self.x = x
        self.y = y
        self.width = 150
        self.height = 150

    def takeDmg(self, dmg):
        self.health -= dmg

# Create Window
displayHeight = 1080
displayWidth = 1920
backgroundColor = (200,200,200)
screen = pygame.display.set_mode((displayWidth, displayHeight))
pygame.display.set_caption("Endless Scroll")


# Import Player1
player1x = 0
player1y = 0
player1yVelocity = 0
player1xVelocity = 0
player1size = 100
playersSpeed = 10
img_player1 = pygame.image.load("img/emeu.jpg").convert()
img_player1 = pygame.transform.scale(img_player1, (100, 100))

#
bg = pygame.image.load("img/back.png").convert()
bg = pygame.transform.scale(bg, (1920, 1080))
bg_width = bg.get_width()

scroll = 0 
tiles = math.ceil(displayWidth / bg_width) + 1


enemy1 = Enemy(800, 800)
enemy2 = Enemy(1200, 200)
enemy3 = Enemy(500, 500)
enemyList = [enemy1, enemy2, enemy3]

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
      screen.blit(bg,(i * bg_width + scroll, 0))

    #scroll background
    scroll -= 5

    #reset scroll
    if abs (scroll) > bg_width:
        scroll = 0


    pressed = pygame.key.get_pressed()
    #PLAYER 1 Y
    if pressed[pygame.K_z]:
        player1yVelocity = -playersSpeed
    elif pressed[pygame.K_s]:
        player1yVelocity = playersSpeed
    else :
        player1yVelocity = 0
    # PLAYER 1 X
    if pressed[pygame.K_d]:
        player1xVelocity = playersSpeed
    elif pressed[pygame.K_q]:
        player1xVelocity = -playersSpeed
    else :
        player1xVelocity = 0

    #Slow
    slow = 0
    if slow == 0 and pressed[pygame.K_LSHIFT]:
        playersSpeed = 5
        slow = 1
    else:
        playersSpeed = 10
        slow = 0

    for enemy in enemyList:
        point = pygame.mouse.get_pos()
        rect = pygame.draw.rect(screen, (255, 255, 255), (enemy.x, enemy.y, enemy.width, enemy.height))
        collide = rect.collidepoint(point)
        if collide:
            enemy.takeDmg(10)
            print(enemy.health)

        if(enemy.health <= 0):
            enemyList.pop(enemyList.index(enemy))

    #Apply player 1 movement
    player1x = player1x + player1xVelocity
    player1y = player1y + player1yVelocity

    # BOUNDING BOX
    # Player 1
    if player1x > displayWidth - player1size:
        player1x = displayWidth - player1size
    elif player1x < 0 :
        player1x = 0
    if player1y > displayHeight - player1size:
        player1y = displayHeight - player1size
    elif player1y < 0 :
        player1y = 0

    #Draw 
    #P1
    screen.blit(img_player1,(player1x, player1y))

    pygame.display.update()
pygame.quit()