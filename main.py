#Import librairies
import pygame
import math
import pygame.time

#Import Classes
from Class.projectile import Projectile
from Class.player import Player
from Class.enemy import Enemy
from Class.score import Score


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

#Import boulles 
classicBullet =  pygame.image.load("img/bullet.png")
classicBullet = pygame.transform.scale(classicBullet, (50, 50))
classicBulletWidth = classicBullet.get_width()

#Bullets & CD
bullets = []
missileCooldown = 0
bulletCoolDown = 0
scoreTime = 0

#Create Player
imgPlayer = pygame.image.load("img/emeu.jpg").convert()
imgPlayer = pygame.transform.scale(imgPlayer, (50, 50))

player = Player(10, 5, 50, displayWidth, displayHeight, 30, 60, 15, 100)

#Create Enemy
imgEnemy = pygame.image.load("img/enemy.png").convert()
imgEnemy = pygame.transform.scale(imgEnemy, (50, 50))

enemy1 = Enemy(50, 2, 300, 0, 50, displayWidth, displayHeight, 100, imgEnemy)
enemy2 = Enemy(50, 2, 1200, 0, 50, displayWidth, displayHeight, 100, imgEnemy)
enemy3 = Enemy(50, 2, 500, 0, 50, displayWidth, displayHeight, 100, imgEnemy)
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
    if pressed[pygame.K_z]:
        player.move(0,-1)
    elif pressed[pygame.K_s]:
        player.move(0,1)
    else :
        playerYVelocity = 0

    # PLAYER X movement
    if pressed[pygame.K_d]:
        player.move(1,0)
    elif pressed[pygame.K_q]:
        player.move(-1,0)
    else :
        playerXVelocity = 0

    # Change each bullet location depending on velocity
    for bullet in bullets:
        if bullet.isHoming == True:
            if len(enemyList) == 0:
                bullet.move(0, -1)
                screen.blit(bullet.image, (bullet.x, bullet.y))
            else:
                dx = enemyList[0].x - bullet.x
                dy = enemyList[0].y - bullet.y

                distance = math.sqrt((dx ** 2) + (dy ** 2))

                # Déplacer le missile vers la cible avec une vitesse constante
                bullet.move((dx / distance), (dy / distance))
                
                # Calculer l'angle de rotation nécessaire pour pointer vers l'ennemi
                angle_radians = math.atan2(dy, dx)
                angle_degrees = math.degrees(angle_radians)

                # Faire pivoter l'image du missile de l'angle calculé
                rotated_image = pygame.transform.rotate(bullet.image, -angle_degrees - 90)

                # Afficher l'image tournée
                screen.blit(rotated_image, (bullet.x, bullet.y))
        else:
            bullet.move(0, -1)
    
    #Enemy
    for enemy in enemyList:
        rect = pygame.Rect(enemy.x, enemy.y, enemy.size, enemy.size)
        screen.blit(enemy.image, (enemy.x, enemy.y))
        if enemy.y > enemy.displayHeight:
            enemy.health = 0
            enemyList.pop(enemyList.index(enemy))

        #Collision bullet & enemy
        for bullet in bullets:
            bulletRect = pygame.Rect(bullet.x, bullet.y, bullet.width, bullet.width)
            if rect.colliderect(bulletRect):
                enemy.takeDmg(bullet.damage)
                score.score_increment(bullet.damage)
                bullets.pop(bullets.index(bullet))

            if(enemy.health <= 0):
                score.score_increment(enemy.score)
                enemyList.pop(enemyList.index(enemy))
                break
        
        playerRect = pygame.Rect(player.X, player.Y, 100, 100)
        if rect.colliderect(playerRect):
            player.takeDmg(10)
            score.score_increment(10)
            enemyList.pop(enemyList.index(enemy))

    #Add a bullet to the bullets list on press
    if pressed[pygame.K_p]:
         if pygame.time.get_ticks() - bulletCoolDown >= 250:
            bullets.append(Projectile(player.X, player.Y, classicBulletWidth, classicBullet, 10, 5, False, displayWidth, displayHeight))
            bulletCoolDown = pygame.time.get_ticks()
    if pressed[pygame.K_o]:
        if pygame.time.get_ticks() - missileCooldown >= 500:
            bullets.append(Projectile(player.X, player.Y, missileWidth, missile, 10, 10, True, displayWidth, displayHeight))
            missileCooldown = pygame.time.get_ticks()

    #Score grows automatically
    if pygame.time.get_ticks() - scoreTime >= 3000:
        score.score_increment(30)
        scoreTime = pygame.time.get_ticks()
        
    #Draw player model on screen
    screen.blit(imgPlayer, (player.X, player.Y))
    
    #Draw each missile model on screen
    for bullet in bullets:
        if bullet.y > 0 - bullet.width and bullet.y < displayHeight and bullet.x > 0 - bullet.width and bullet.x < displayWidth:  
            if bullet.isHoming == False:
                screen.blit(bullet.image, (bullet.x, bullet.y))
        else:
            bullets.pop(bullets.index(bullet))

    scoreText = font.render(f'Score: {score.score}', True, (255, 255, 255))
    screen.blit(scoreText, (10, 10))
    pygame.display.update()

pygame.quit()
