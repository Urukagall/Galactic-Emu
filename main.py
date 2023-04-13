# Init
print("Hello Today I'm Gonna Teach You")
import pygame
import math
import pygame.time
from Class.projectile import Projectile
from Class.player import Player
from Class.enemy import Enemy

pygame.init()
clock = pygame.time.Clock()

# Create Window
displayHeight = 1080
displayWidth = 1920
backgroundColor = (200,200,200)
screen = pygame.display.set_mode((displayWidth, displayHeight))
pygame.display.set_caption("Endless Scroll")


#Import background model

backGround = pygame.image.load("img/back.png").convert()
backGround = pygame.transform.scale(backGround, (1920, 1080))
backGround_height = backGround.get_height()

scroll = 0 
tiles = math.ceil(displayHeight / backGround_height) + 1

#Import missile model
missile = pygame.image.load("img/missile.png")
missile = pygame.transform.scale(missile, (100, 100))
missile_width = missile.get_width()

#Make scrolling background effect
scroll = 0 
tiles = math.ceil(displayHeight / backGround_height) + 1

#Bullets & CD
bullets = []
start_time = 0

#Create Player
img_player = pygame.image.load("img/emeu.jpg").convert()
img_player = pygame.transform.scale(img_player, (100, 100))

player = Player(10, 5, 100, pygame.transform.scale(pygame.image.load("img/emeu.jpg").convert(), (100, 100)), displayWidth, displayHeight, 30, 60, 15)

enemy1 = Enemy(800, 800)
enemy2 = Enemy(1200, 200)
enemy3 = Enemy(500, 500)
enemyList = [enemy1, enemy2, enemy3]

timerDash = [0 , 0]

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
    
     #draw scrolling background 
    for i in range(0, tiles):
      screen.blit(backGround,(0,(-1 * i) * backGround_height - scroll))

    #scroll background
    scroll -= 5

    #reset scroll
    if abs (scroll) > backGround_height:
        scroll = 0


    pressed = pygame.key.get_pressed()

    if pressed[pygame.K_LSHIFT]:
        player.speed = player.slowSpeed
    elif pressed[pygame.K_SPACE] and timerDash[1] == 0:
        timerDash[1] = player.cooldownDash
        timerDash[0] = player.timeDash
        player.speed = player.dashSpeed
    elif timerDash[0] == 0: 
        player.speed = player.basicSpeed


    if timerDash[0] > 0:
        timerDash[0] -= 1
    elif timerDash[0] == 0 and timerDash[1] > 0:
        timerDash[1] -= 1

    #PLAYER Y
    if pressed[pygame.K_z]:
        player.move(0,-1)
    elif pressed[pygame.K_s]:
        player.move(0,1)
    else :
        playerYVelocity = 0
    # PLAYER X
    if pressed[pygame.K_d]:
        player.move(1,0)
    elif pressed[pygame.K_q]:
        player.move(-1,0)
    else :
        playerXVelocity = 0

    # Change each bullet location depending on velocity
    for bullet in bullets:
        bullet.y -= bullet.velocity
    
    # Enemy
    for enemy in enemyList:
        rect = pygame.draw.rect(screen, (255, 255, 255), (enemy.x, enemy.y, enemy.width, enemy.height))

        for bullet in bullets:
            if rect.collidepoint(bullet.x,bullet.y) or rect.collidepoint(bullet.x + 100,bullet.y):
                enemy.takeDmg(10)
                bullets.pop(bullets.index(bullet))

            if(enemy.health <= 0):
                enemyList.pop(enemyList.index(enemy))

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
