# Init
print("Hello Today I'm Gonna Teach You")
import pygame
import math
import pygame.time
from Class.projectile import Projectile
from Class.player import Player

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
backGround_width = backGround.get_width()

#Import missile model
missile = pygame.image.load("img/missile.png")
missile = pygame.transform.scale(missile, (100, 100))
missile_width = missile.get_width()

#Make scrolling background effect
scroll = 0 
tiles = math.ceil(displayWidth / backGround_width) + 1

#Bullets & CD
bullets = []
start_time = 0


player = Player(10, 5, 100, pygame.transform.scale(pygame.image.load("img/emeu.jpg").convert(), (100, 100)), displayWidth, displayHeight)

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
      screen.blit(backGround,(i * backGround_width + scroll, 0))

    #Scroll background speed
    scroll -= 5

    #reset scroll
    if abs (scroll) > backGround_width:
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

    #Change each bullet location depending on velocity
    for bullet in bullets:
        bullet.y -= bullet.velocity
    
    #Add a bullet to the bullets list on press
    if pressed[pygame.K_p]:
        if pygame.time.get_ticks() - start_time >= 500:
            bullets.append(Projectile(player.X, player.Y, missile_width, missile))
            start_time = pygame.time.get_ticks()
        
    #Draw player model on screen
    screen.blit(player.img, (player.X, player.Y))
    
    #Draw each missile model on screen
    for bullet in bullets:
        if bullet.y > 0 & bullet.y < 1920:
            screen.blit(bullet.image, (bullet.x, bullet.y))
        else:
            bullets.pop(bullets.index(bullet))

    pygame.display.update()
pygame.quit()
