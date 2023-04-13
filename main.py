# Init
print("Hello Today I'm Gonna Teach You")
import pygame
import math
import pygame.time
from Class/projectile import Projectile
from Class/player import Player
pygame.init()
clock = pygame.time.Clock()

# Create Window
displayHeight = 1080
displayWidth = 1920
backgroundColor = (200,200,200)
screen = pygame.display.set_mode((displayWidth, displayHeight))
pygame.display.set_caption("Endless Scroll")


#Create Player
playerx = 0
playery = 0
playerxVelocity = 0
playeryVelocity = 0
playersize = 100
playerSpeed = 10
img_player = pygame.image.load("img/emeu.jpg").convert()
img_player = pygame.transform.scale(img_player, (100, 100))

#Import background model
backGround = pygame.image.load("img/back.png").convert()
backGround = pygame.transform.scale(backGround, (1920, 1080))
backGround_width = bg.get_width()

#Import missile model
missile = pygame.image.load("img/missile.png")
missile = pygame.transform.scale(missile, (100, 100))
missile_width = missile.get_width()

#Make scrolling background effect
scroll = 0 
tiles = math.ceil(displayWidth / bg_width) + 1

#Bullets & CD
bullets = []
start_time = 0

# Main Loop
running = True
while running:
    # run the game at a constant 60fps
    clock.tick(60)
    #Close window on Escape press
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            running=False
        elif events.type == pygame.KEYDOWN:
            if events.key == pygame.K_ESCAPE:
                running=False
    
    #Draw the scrolling background 
    for i in range(0, tiles):
      screen.blit(bg,(i * bg_width + scroll, 0))

    #Scroll background speed
    scroll -= 5

    #reset scroll
    if abs (scroll) > bg_width:
        scroll = 0


    pressed = pygame.key.get_pressed()
    #PLAYER Y
    if pressed[pygame.K_z]:
        playeryVelocity = -playersSpeed
    elif pressed[pygame.K_s]:
        playeryVelocity = playersSpeed
    else :
        playeryVelocity = 0
    # PLAYER X
    if pressed[pygame.K_d]:
        playerxVelocity = playersSpeed
    elif pressed[pygame.K_q]:
        playerxVelocity = -playersSpeed
    else :
        playerxVelocity = 0

    #Apply player movement
    playerx = playerx + playerxVelocity
    playery = playery + playeryVelocity

    # BOUNDING BOX
    # Player
    if playerx > displayWidth - playersize:
        playerx = displayWidth - playersize
    elif playerx < 0 :
        playerx = 0
    if playery > displayHeight - playersize:
        playery = displayHeight - playersize
    elif playery < 0 :
        playery = 0
        
    if pressed[pygame.K_LSHIFT]:
        player.speed = player.slowSpeed
    else: 
        player.speed = player.basicSpeed

    #Change each bullet location depending on velocity
    for bullet in bullets:
        bullet.y -= bullet.velocity
    
    #Add a bullet to the bullets list on press
    if pressed[pygame.K_p]:
        if pygame.time.get_ticks() - start_time >= 500:
            bullets.append(Projectile(player1x, player1y, missile_width, missile))
            start_time = pygame.time.get_ticks()
        
    #Draw player model on screen
    screen.blit(img_player,(playerx, playery))
    
    #Draw each missile model on screen
    for bullet in bullets:
        if bullet.y > 0 & bullet.y < 1920:
            screen.blit(bullet.image, (bullet.x, bullet.y))
        else:
            bullets.pop(bullets.index(bullet))

    pygame.display.update()
pygame.quit()
