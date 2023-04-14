# Init
print("Hello Today I'm Gonna Teach You")
import pygame
import math
import pygame.time
from Class.projectile import Projectile
from Class.player import Player
from Class.enemy import Enemy
from Class.score import Score

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
missile = pygame.transform.scale(missile, (50, 50))
missile_width = missile.get_width()

#Bullets & CD
bullets = []
start_time = 0
score_time = 0

#Create Player
img_player = pygame.image.load("img/emeu.jpg").convert()
img_player = pygame.transform.scale(img_player, (50, 50))

#Create Enemy
img_enemy = pygame.image.load("img/enemy.png").convert()
img_enemy = pygame.transform.scale(img_enemy, (50, 50))

player = Player(10, 5, 50, pygame.transform.scale(pygame.image.load("img/emeu.jpg").convert(), (50, 50)), displayWidth, displayHeight, 30, 60, 15, 100)

enemy1 = Enemy(50, 2, 300, 0, 50, displayWidth, displayHeight, 100)
enemy2 = Enemy(50, 2, 1200, 0, 50, displayWidth, displayHeight, 100)
enemy3 = Enemy(50, 2, 500, 0, 50, displayWidth, displayHeight, 100)
enemyList = [enemy1, enemy2, enemy3]

timerDash = [0 , 0]

score = Score()
#score = 0
#score_increment = 10

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
      screen.blit(backGround,(0,(-1 * i) * backGround_height - scroll))

    #scroll background
    scroll -= 5

    #reset scroll
    if abs (scroll) > backGround_height:
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
        bullet.y -= bullet.velocity
    
    # Enemy
    for enemy in enemyList:
        enemy.move(0, 1)
        rect = pygame.Rect(enemy.x, enemy.y, enemy.size, enemy.size)
        screen.blit(img_enemy, (enemy.x, enemy.y))
        if enemy.y > enemy.displayHeight:
            enemyList.pop(enemyList.index(enemy))

        for bullet in bullets:
            bullet_rect = pygame.Rect(bullet.x, bullet.y, bullet.width, bullet.width)
            if rect.colliderect(bullet_rect):
                enemy.takeDmg(10)
                score.score_increment(10)
                bullets.pop(bullets.index(bullet))

            if(enemy.health <= 0):
                score.score_increment(enemy.score)
                enemyList.pop(enemyList.index(enemy))
                break
        
        player_rect = pygame.Rect(player.X, player.Y, 100, 100)
        if rect.colliderect(player_rect):
            player.takeDmg(10)
            score.score_increment(10)
            enemyList.pop(enemyList.index(enemy))

    #Add a bullet to the bullets list on press
    if pressed[pygame.K_p]:
        if pygame.time.get_ticks() - start_time >= 500:
            bullets.append(Projectile(player.X, player.Y, missile_width, missile))
            start_time = pygame.time.get_ticks()

    #Score grows automatically
    if pygame.time.get_ticks() - score_time >= 3000:
        score.score_increment(30)
        score_time = pygame.time.get_ticks()
        
    #Draw player model on screen
    screen.blit(player.img, (player.X, player.Y))
    
    #Draw each missile model on screen
    for bullet in bullets:
        if bullet.y > 0 & bullet.y < 1920 :
            screen.blit(bullet.image, (bullet.x, bullet.y))
        else:
            bullets.pop(bullets.index(bullet))

    score_text = font.render(f'Score: {score.score}', True, (255, 255, 255))
    screen.blit(score_text, (10, 10))
    pygame.display.update()
pygame.quit()
