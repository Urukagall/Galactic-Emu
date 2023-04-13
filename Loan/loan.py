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
      screen.blit(bg,(0, i * bg_height + scroll))

    #scroll background
    scroll -= 5

    #reset scroll
    if abs (scroll) > bg_height:
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