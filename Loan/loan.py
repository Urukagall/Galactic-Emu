
#Import librairies
import pygame
import math
import pygame.time
import random

#Import Classes
from Class.projectile import Projectile
from Class.player import Player
from Class.enemy import Enemy
from Class.score import Score
from Class.button import Button

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
pygame.display.set_caption("Bullet Hell")

#Import background model
backGround = pygame.image.load("img/back.png").convert()
backGround = pygame.transform.scale(backGround, (displayWidth, displayWidth))
backGroundHeight = backGround.get_height()
backGroundWidth = backGround.get_width()

#Pre-requisite for the screen scrolling
trueScroll = 0 
tiles = math.ceil(displayHeight / backGroundHeight) + 1

#Import missile model
missile = pygame.image.load("img/missile.png")
missile = pygame.transform.scale(missile, (missile.get_width(), missile.get_height()))
missileWidth = missile.get_width()

#Import bullets 
classicBullet =  pygame.image.load("img/bullet.png")
classicBullet = pygame.transform.scale(classicBullet, (classicBullet.get_width()*2, classicBullet.get_height()*2))
bigBall = pygame.image.load("img/grosse_boule.png")
bigBall = pygame.transform.scale(bigBall, (50, 50))

#Import ultimate
ultimateShoot = pygame.image.load("img/grosse_boule.png")
ultimateShoot = pygame.transform.scale(ultimateShoot, (100, 100))
ultimateShootWidth = ultimateShoot.get_width()

ultimateSound = pygame.mixer.Sound("sound/seismic_charge.mp3")

#projectileList & CD
projectileList = []
missileCooldown = 0
bulletCoolDown = 0
ultimateCooldown = 0
scoreTime = 0

particleList = []
shaking = False
screenShake = 40

#Create Player
imgPlayer = pygame.image.load("img/player.png")
imgPlayer = pygame.transform.scale(imgPlayer, (50, 50))

player = Player(10, 5, 50, displayWidth, displayHeight, 30, 60, 15, 5, projectileList)


#Create Enemy
#Load different images
imgRailgun = pygame.image.load("img/railgun.png")
imgRailgun = pygame.transform.scale(imgRailgun, (50, 50))
imgEnemy = pygame.image.load("img/bozo.png")
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

# Font importe

font = pygame.font.Font(None, 36)

def rotate(image, rect, angle):
    """Rotate the image while keeping its center."""
    # Rotate the original image without modifying it.
    new_image = pygame.transform.rotate(image, angle)
    # Get a new rect with the center of the old rect.
    rect = new_image.get_rect(center=rect.center)
    return new_image, rect

while running:
    # run the game at a constant 60fps
    clock.tick(60)

    font = pygame.font.Font(None, 36)
    
    #Close window on Escape press
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            running=False
        elif events.type == pygame.KEYDOWN:
            if events.key == pygame.K_ESCAPE:
                running=False
        if events.type == pygame.MOUSEBUTTONDOWN:
            for button in buttonList:
                button.checkForInput(pygame.mouse.get_pos(), player)
        for button in buttonList:
            button.changeColor(pygame.mouse.get_pos())
    # Play music in Loop
    
     #draw scrolling background
    
    scroll = int(trueScroll)

    #screen shake
    if shaking:
        scroll += random.randint(0, screenShake) - screenShake/2

    for i in range(0, tiles):
        screen.blit(backGround, (0, i * displayWidth + scroll))
    trueScroll -= 1
    #reset scroll
    if abs(trueScroll) > displayWidth:
        trueScroll = 0

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
                bulletRect = pygame.Rect(bullet.x, bullet.y, bullet.size, bullet.size)
                if playerRect.colliderect(bulletRect):
                    player.getHit()
                    projectileList.pop(projectileList.index(bullet))
    

    #Enemy
    for enemy in enemyList:
        enemy.update(player)
        rect = pygame.Rect(enemy.x, enemy.y, enemy.size, enemy.size)
        
        screen.blit(enemy.image, (enemy.x, enemy.y))
        if enemy.y > enemy.displayHeight:
            enemy.health = 0
            enemyList.pop(enemyList.index(enemy))

        #Collision bullet & enemy
        for bullet in projectileList:
            if bullet.isPlayer == True:
                bulletRect = pygame.Rect(bullet.x, bullet.y, bullet.size, bullet.size)
                if rect.colliderect(bulletRect):
                    enemy.takeDmg(bullet.damage, enemyList)
                    score.score_increment(10)
                    projectileList.pop(projectileList.index(bullet))

                if(enemy.health <= 0):
                    score.score_increment(enemy.score)
                    #enemyList.pop(enemyList.index(enemy))
                    break
        if rect.colliderect(playerRect):
            player.getHit()
            score.score_increment(10)
            enemyList.pop(enemyList.index(enemy))

    for particle in particleList:
        if(particle.draw(screen, projectileList)):
            particleList.pop(particleList.index(particle))
            shaking = False
        else:
            shaking = True
        
        if(particle.doDamage):
            for enemy in enemyList:
                enemy.takeDmg(player.ultimateDmg, enemyList)

    #Add a bullet to the projectileList list on press
    if pressed[pygame.K_w]:
        if player.cooldown <= 0:
            player.shoot()
            player.cooldown = player.timeBetweenShots
    if pressed[pygame.K_x]:
        if player.missileCooldown <= 0:
            player.shootHoming()
            player.missileCooldown = player.timeBetweenMissiles
    if pressed[pygame.K_c]:
        if player.ultimateCooldown <= 0:
            #play sfx
            ultimateSound.play()
            player.shootUltimate(particleList)
            player.ultimateCooldown = player.timeBetweenUltimates
    
    player.cooldown -= 1
    player.missileCooldown -= 1
    player.ultimateCooldown -= 1

    

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
    ultimateText = font.render(f'Ultimate in: {math.ceil(player.ultimateCooldown/60)}', True, (255, 255, 255))
    screen.blit(ultimateText, (10, 50))
    pygame.display.update()


pygame.display.set_caption("Menu")


# def get_font(size): # Returns Press-Start-2P in the desired size
#     return pygame.font.Font("assets/font.ttf", size)


# def play():
#     while True:
#         PLAY_MOUSE_POS = pygame.mouse.get_pos()

#         screen.fill("black")

#         PLAY_TEXT = get_font(45).render("This is the PLAY screen.", True, "White")
#         PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 260))
#         screen.blit(PLAY_TEXT, PLAY_RECT)

#         PLAY_BACK = Button(image=None, pos=(640, 460), 
#                             text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")

#         PLAY_BACK.changeColor(PLAY_MOUSE_POS)
#         PLAY_BACK.update(screen)

#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
#                     main_menu()

#         pygame.display.update()
    
# def options():
#     while True:
#         OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

#         screen.fill("white")

#         OPTIONS_TEXT = get_font(45).render("This is the OPTIONS screen.", True, "Black")
#         OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
#         screen.blit(OPTIONS_TEXT, OPTIONS_RECT)

#         OPTIONS_BACK = Button(image=None, pos=(640, 460), 
#                             text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

#         OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
#         OPTIONS_BACK.update(screen)

#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
#                     main_menu()

#         pygame.display.update()


# def main_menu():
#     while True:
#         screen.blit(backGround, (0, 0))

#         MENU_MOUSE_POS = pygame.mouse.get_pos()

#         MENU_TEXT = get_font(100).render("MAIN MENU", True, "#b68f40")
#         MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

#         PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 250), 
#                             text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
#         OPTIONS_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 400), 
#                             text_input="OPTIONS", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
#         QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(640, 550), 
#                             text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

#         screen .blit(MENU_TEXT, MENU_RECT)

#         for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
#             button.changeColor(MENU_MOUSE_POS)
#             button.update(screen)
        
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
#                     play()
#                 if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
#                     options()
#                 if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
#                     pygame.quit()
#                     sys.exit()

#         pygame.display.update()

# main_menu()


pygame.quit()