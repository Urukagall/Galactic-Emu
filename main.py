#Import librairies
import pygame
import math
import pygame.time

#Import Classes
from Class.projectile import Projectile
from Class.player import Player
from Class.enemy import Enemy
from Class.score import Score

#Import Patterns
from Pattern.enemiesPattern import *

#Init the pygame & clock
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
backGroundHeight = backGround.get_height()

#Pre-requisite for the screen scrolling
scroll = 0 
tiles = math.ceil(displayHeight / backGroundHeight) + 1

#Import missile model
missile = pygame.image.load("img/missile.png")
missile = pygame.transform.scale(missile, (50, 50))
missileWidth = missile.get_width()

#Import bullets 
classicBullet =  pygame.image.load("img/bullet.png")
classicBullet = pygame.transform.scale(classicBullet, (50, 50))
classicBulletWidth = classicBullet.get_width()

#Import ultimate
ultimateShoot = pygame.image.load("img/grosse_boule.png")
ultimateShoot = pygame.transform.scale(ultimateShoot, (100, 100))
ultimateShootWidth = ultimateShoot.get_width()

#projectileList & CD
projectileList = []
missileCooldown = 0
bulletCoolDown = 0
ultimateCooldown = 0
scoreTime = 0

#Create Player
imgPlayer = pygame.image.load("img/player.png")
imgPlayer = pygame.transform.scale(imgPlayer, (50, 50))

player = Player(10, 5, 50, displayWidth, displayHeight, 30, 60, 15, 5, projectileList)


#Create Enemy
imgEnemy = pygame.image.load("img/enemy.png").convert()
imgEnemy = pygame.transform.scale(imgEnemy, (50, 50))

enemy1 = Enemy(50, 2, 300, 0, 50, displayWidth, displayHeight, 100, imgEnemy, 10, 4, math.pi/2, projectileList, 1, "left")
enemy2 = Enemy(50, 2, 1200, 0, 50, displayWidth, displayHeight, 100, imgEnemy, 10, 4, math.pi/2, projectileList, 1, "left")
enemy3 = Enemy(50, 2, 500, 0, 50, displayWidth, displayHeight, 100, imgEnemy, 10, 4, math.pi/2, projectileList, 1, "left")
enemyList = [enemy1, enemy2, enemy3]


#Initiate dash coordinates
timerDash = [0 , 0]

#Initiate score
score = Score()

# Main Loop
running = True
while running:
    font = pygame.font.Font(None, 36)
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
      screen.blit(backGround,(0,(-1 * i) * backGroundHeight - scroll))

    #scroll background
    scroll -= 5

    #reset scroll
    if abs (scroll) > backGroundHeight:
        scroll = 0

    # Slow movement and dash
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

     #PLAYER Y movement
    if pressed[pygame.K_UP]:
        velY = -1
    elif pressed[pygame.K_DOWN]:
        velY = 1
    else :
        velY = 0

    # PLAYER X movement
    if pressed[pygame.K_RIGHT]:
        velX = 1
    elif pressed[pygame.K_LEFT]:
        velX = -1
    else :
        velX = 0
        
    player.move(velX, velY)
    playerRect = pygame.Rect(player.X, player.Y, player.size/2, player.size/2)

    for bullet in projectileList:
        if bullet.update(enemyList) == True:
            projectileList.pop(projectileList.index(bullet))
        screen.blit(bullet.image, (bullet.x, bullet.y))
        #Collision bullet & enemy
        for bullet in projectileList:
            if bullet.isPlayer == False:
                bulletRect = pygame.Rect(bullet.x, bullet.y, bullet.width, bullet.width)
                if playerRect.colliderect(bulletRect):
                    player.getHit()
                    projectileList.pop(projectileList.index(bullet))

    #Enemy
    for enemy in enemyList:
        enemy.update()
        rect = pygame.Rect(enemy.x, enemy.y, enemy.size, enemy.size)
        
        screen.blit(enemy.image, (enemy.x, enemy.y))
        if enemy.y > enemy.displayHeight:
            enemy.health = 0
            enemyList.pop(enemyList.index(enemy))

        #Collision bullet & enemy
        for bullet in projectileList:
            if bullet.isPlayer == True:
                bulletRect = pygame.Rect(bullet.x, bullet.y, bullet.width, bullet.width)
                if rect.colliderect(bulletRect):
                    enemy.takeDmg(bullet.damage)
                    score.score_increment(10)
                    projectileList.pop(projectileList.index(bullet))

                if(enemy.health <= 0):
                    score.score_increment(enemy.score)
                    enemyList.pop(enemyList.index(enemy))
                    break
        if rect.colliderect(playerRect):
            player.takeDmg(10)
            score.score_increment(10)
            enemyList.pop(enemyList.index(enemy))


    #Add a bullet to the projectileList list on press
    if pressed[pygame.K_w]:
        if player.cooldown <= 0:
            player.shoot()
            player.cooldown = player.timeBetweenShots
    if pressed[pygame.K_x]:
        if player.missileCooldown <= 0:
            player.shootHoming()
            player.missileCooldown = player.timeBetweenMissiles
    
    player.cooldown -= 1
    player.missileCooldown -= 1

    #Shoot your ultimate
    if pressed[pygame.K_i]:
        if pygame.time.get_ticks() - ultimateCooldown >= 20000:
            player.shoot()
            player.ultimateCooldown = player.timeBetweenUltimates

    #Score grows automatically
    if pygame.time.get_ticks() - scoreTime >= 3000:
        score.score_increment(30)
        scoreTime = pygame.time.get_ticks()
        
    #Draw player model on screen
    screen.blit(imgPlayer, (player.X, player.Y))
    
    #Write player's score & remaining lives
    scoreText = font.render(f'Score: {score.score}', True, (255, 255, 255))
    screen.blit(scoreText, (10, 10))
    livesText = font.render(f'Lives: {player.lives}', True, (255, 255, 255))
    screen.blit(livesText, (10, 30))
    pygame.display.update()

pygame.quit()