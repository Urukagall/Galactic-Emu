import pygame, sys
import math
import pygame.time
import random
# import cv2

from Class.projectile import Projectile
from Class.player import Player
from Class.enemy import Enemy
from Class.score import Score
from Class.button import Button
from Class.boss import Boss
from Functions.saveReader import *


from Functions.enemiesPattern import *
# from Functions.transition import *

def drawTransition(surf, y, color):
    for x in range(16):
        pygame.draw.rect(surf, color, (x,16-y,1,y))
        y -= 1

def darken(image, percent = 50):
    '''Creates a  darkened copy of an image, darkened by percent (50% by default)'''
    newImg = image.copy()
    dark = pygame.Surface(newImg.get_size()).convert_alpha()
    newImg.set_colorkey((0,0,0))
    dark.fill((0,0,0,percent/100*255))
    newImg.blit(dark, (0,0))
    return newImg

def rotate(image, rect, angle):
        """Rotate the image while keeping its center."""
        # Rotate the original image without modifying it.
        newImage = pygame.transform.rotate(image, angle)
        # Get a new rect with the center of the old rect.
        rect = newImage.get_rect(center=rect.center)
        return newImage, rect

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("font.ttf", size)

def createEnemy(data, bulletRotation=0, bulletSpeed2=0, arrayNumber2=0,angleBetweenArrays2=0,timeBetweenShots2=0,bulletImg2=[],aimAtPlayer2=False,bulletRotation2=0,pattern = firstPattern):
    '''money = data[15]
    bulletRotation = data[16]
    bulletSpeed2 = data[17]
    arrayNumber2 = data[18]
    angleBetweenArrays2 = data[19]
    timeBetweenShots2 = data[20]
    bulletImg2 = data[21]
    aimAtPlayer2 = data[22]
    bulletRotation2 = data[23]
    pattern = data[24]'''
    newEnemy = Enemy(data[0],data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[9], data[10], data[11], data[12], data[13], data[14], data[15], data[16], data[17], bulletRotation, bulletSpeed2, arrayNumber2, angleBetweenArrays2, timeBetweenShots2, bulletImg2, aimAtPlayer2, bulletRotation2, pattern)
    return newEnemy

def play(player, gameManager):
    pygame.init()
    clock = pygame.time.Clock()

    # Create Window
    displayHeight = 1080
    displayWidth = 1920
    screen = pygame.display.set_mode((displayWidth, displayHeight))
    pygame.display.set_caption("Bullet Hell")

    #Import background model
    levelBackGround = pygame.image.load("img/assets/back.png").convert()
    levelBackGround = pygame.transform.scale(levelBackGround, (1920, 1080))
    backGroundHeight = levelBackGround.get_height()
    backGroundWidth = levelBackGround.get_width()

    #Import boss' base asset
    bossBase = pygame.image.load("img/assets/base-bg.png").convert()
    bossBase = pygame.transform.scale(bossBase, (1920, 1080))


    backGround = levelBackGround

    #Transitions variables
    transition = False
    transitionY = 0
    subY = 0
    transitionSurf = pygame.Surface((16,9))
    transitionSurf.set_colorkey((0,0,0))

    #Pre-requisite for the screen scrolling
    trueScroll = 0 
    tilesHeight = math.ceil(displayHeight / backGroundHeight) + 1
    tilesWidth = math.ceil(displayWidth / backGroundWidth) + 1

    #Import bullets 
    '''Blue bullets import'''
    ballBlue = pygame.image.load("img/bullets/ball.png").convert_alpha()
    ballBlue = pygame.transform.scale(ballBlue, (ballBlue.get_width()*2, ballBlue.get_height()*2))

    bigBallBlue = pygame.image.load("img/bullets/bigBall.png").convert_alpha()
    bigBallBlue = pygame.transform.scale(bigBallBlue, (50,50))

    bulletBlue =  pygame.image.load("img/bullets/bullet.png").convert_alpha()
    bulletBlue = pygame.transform.scale(bulletBlue, (bulletBlue.get_width()*2, bulletBlue.get_height()*2))

    carreauBlue = pygame.image.load("img/bullets/carreau.png").convert_alpha()
    carreauBlue = pygame.transform.scale(carreauBlue, (carreauBlue.get_width()*2, carreauBlue.get_height()*2))

    missileBlue = pygame.image.load("img/bullets/missile.png").convert_alpha()
    missileBlue = pygame.transform.scale(missileBlue, (missileBlue.get_width(), missileBlue.get_height()))

    '''Red bullets import'''
    ballRed = pygame.image.load("img/bullets/ball_red.png").convert_alpha()
    ballRed = pygame.transform.scale(ballRed, (ballRed.get_width()*2, ballRed.get_height()*2))

    bigBallRed = pygame.image.load("img/bullets/bigBall_red.png").convert_alpha()
    bigBallRed = pygame.transform.scale(bigBallRed, (50,50))

    bulletRed = pygame.image.load("img/bullets/bullet_red.png").convert_alpha()
    bulletRed = pygame.transform.scale(bulletRed, (bulletRed.get_width()*2, bulletRed.get_height()*2))

    carreauRed = pygame.image.load("img/bullets/carreau_red.png").convert_alpha()
    carreauRed = pygame.transform.scale(carreauRed, (carreauRed.get_width()*2, carreauRed.get_height()*2))

    missileRed = pygame.image.load("img/bullets/missile_red.png").convert_alpha()
    missileRed = pygame.transform.scale(missileRed, (missileRed.get_width(), missileRed.get_height()))

    '''Green bullets import'''
    ballGreen = pygame.image.load("img/bullets/ball_green.png").convert_alpha()
    ballGreen = pygame.transform.scale(ballGreen, (ballGreen.get_width()*2, ballGreen.get_height()*2))

    bigBallGreen = pygame.image.load("img/bullets/bigBall_green.png").convert_alpha()
    bigBallGreen = pygame.transform.scale(bigBallGreen, (50, 50))

    bulletGreen =  pygame.image.load("img/bullets/bullet_green.png").convert_alpha()
    bulletGreen = pygame.transform.scale(bulletGreen, (bulletGreen.get_width()*2, bulletGreen.get_height()*2))

    carreauGreen =  pygame.image.load("img/bullets/carreau_green.png").convert_alpha()
    carreauGreen = pygame.transform.scale(carreauGreen, (carreauGreen.get_width()*2, carreauGreen.get_height()*2))

    missileGreen = pygame.image.load("img/bullets/missile_green.png").convert_alpha()
    missileGreen = pygame.transform.scale(missileGreen, (missileGreen.get_width(), missileGreen.get_height()))
    '''Purple bullets import'''
    ballPurple = pygame.image.load("img/bullets/ball_purple.png").convert_alpha()
    ballPurple = pygame.transform.scale(ballPurple, (ballPurple.get_width()*2, ballPurple.get_height()*2))

    bigBallPurple = pygame.image.load("img/bullets/bigBall_purple.png").convert_alpha()
    bigBallPurple = pygame.transform.scale(bigBallPurple, (50, 50))

    bulletPurple =  pygame.image.load("img/bullets/bullet_purple.png").convert_alpha()
    bulletPurple = pygame.transform.scale(bulletPurple, (bulletPurple.get_width()*2, bulletPurple.get_height()*2))

    carreauPurple =  pygame.image.load("img/bullets/carreau_purple.png").convert_alpha()
    carreauPurple = pygame.transform.scale(carreauPurple, (carreauPurple.get_width()*2, carreauPurple.get_height()*2))

    missilePurple = pygame.image.load("img/bullets/missile_purple.png").convert_alpha()
    missilePurple = pygame.transform.scale(missilePurple, (missilePurple.get_width(), missilePurple.get_height()))

    '''Yellow bullets import'''
    ballYellow = pygame.image.load("img/bullets/ball_yellow.png").convert_alpha()
    ballYellow = pygame.transform.scale(ballYellow, (ballYellow.get_width()*2, ballYellow.get_height()*2))

    bigBallYellow = pygame.image.load("img/bullets/bigBall_yellow.png").convert_alpha()
    bigBallYellow = pygame.transform.scale(bigBallYellow, (50, 50))

    bulletYellow =  pygame.image.load("img/bullets/bullet_yellow.png").convert_alpha()
    bulletYellow = pygame.transform.scale(bulletYellow, (bulletYellow.get_width()*2, bulletYellow.get_height()*2))

    carreauYellow =  pygame.image.load("img/bullets/carreau_yellow.png").convert_alpha()
    carreauYellow = pygame.transform.scale(carreauYellow, (carreauYellow.get_width()*2, carreauYellow.get_height()*2))

    missileYellow = pygame.image.load("img/bullets/missile_yellow.png").convert_alpha()
    missileYellow = pygame.transform.scale(missileYellow, (missileYellow.get_width(), missileYellow.get_height()))

    #Import ultimate' sound effect
    ultimateSound = pygame.mixer.Sound("sound/seismic_charge.mp3")
    ultimateSound.set_volume(0.2 * gameManager.sound)

    # Import Music
    bulletHellSound = pygame.mixer.Sound("sound/Bullet_Hell.mp3")
    bulletHellSound.set_volume(0.2 * gameManager.sound)
    bossMusic = pygame.mixer.Sound("sound/bossFight.mp3")
    bossMusic.set_volume(0.2 * gameManager.sound)

    #projectileList & CD
    projectileList = []
    scoreTime = 0

    particleList = []
    shaking = False
    screenShake = 40

    #Redefine player & its bullets luminosity
    imgPlayerAvatar = pygame.image.load("img/avatar/playerAvatar.png").convert_alpha()
    imgPlayerAvatar = pygame.transform.scale(imgPlayerAvatar, (150, 150))
    imgPlayerAvatarDamage = pygame.image.load("img/avatar/playerAvatarDamage.png").convert_alpha()
    imgPlayerAvatarDamage = pygame.transform.scale(imgPlayerAvatarDamage, (150, 150))
    imgPlayer = pygame.image.load("img/ships/player.png").convert_alpha()
    imgPlayer = pygame.transform.scale(imgPlayer, (50, 50))
    playerShield = pygame.image.load("img/ships/playerShield.png").convert_alpha()
    playerShield = pygame.transform.scale(playerShield, (50, 50))
    invincible = False
    invincibleCountdown = 0
    damageAvatarCountdown = 0
    isPlaying = False

    # darkCarreau = darken(carreauBlue,45).convert_alpha()
    # darkBullet = darken(bulletBlue).convert_alpha()
    # darkMissile = darken(missileBlue,60).convert_alpha()

    # player = Player(10, 5, 50, 1920, 1080, 30, 60, 15, 5, projectileList, bulletBlue, missileBlue, carreauBlue)

    player.projectileList = projectileList
    player.redefined()

    #Load different images for enemies
    imgRailgun = pygame.image.load("img/ships/railgun.png").convert_alpha()
    imgRailgun = pygame.transform.scale(imgRailgun, (50, 50))
    imgBozo = pygame.image.load("img/ships/bozo.png").convert_alpha()
    imgBozo = pygame.transform.scale(imgBozo, (50, 50))
    imgMiniBozo = pygame.image.load("img/ships/bozo.png").convert_alpha()
    imgMiniBozo = pygame.transform.scale(imgBozo, (25, 25))
    imgSupressor = pygame.image.load("img/ships/supressor.png").convert_alpha()
    imgSupressor = pygame.transform.scale(imgSupressor, (50,50))
    imgSpyral = pygame.image.load("img/ships/spyral.png").convert_alpha()
    imgSpyral = pygame.transform.scale(imgSpyral, (50,50))
    imgMiniBoss = pygame.image.load("img/ships/mini_boss.png").convert_alpha()
    imgMiniBoss = pygame.transform.scale(imgMiniBoss, (100,100))

    #Create Enemy
    "[aimAtEnemy, HP, speed, x, y, size, displayWidth, displayHeight, score, image, bulletImg, bulletSpeed, arrayNumber, angleBetweenArrays, projectileList, timeBetweenShots, facing, ||optionals from now|| money, bulletRotation, bulletSpeed2, arrayNumber2, angleBetweenArrays2, timeBetweenShots2, bulletImg2, aimAtPlayer2, bulletRotation2, pattern"
    miniBozo = [True, 10, 0.5, 1200, 0, 50, displayWidth, displayHeight, 100, imgMiniBozo, bulletRed, 10, 1, 0, projectileList, 3, "left", 10]
    bozo = [True, 100, 2, 1200, 0, 50, displayWidth, displayHeight, 100, imgBozo, bulletRed, 10, 1, 0, projectileList, 1, "left", 20]
    railgun = [True, 300, 0.5, 300, 0, 50, displayWidth, displayHeight, 100, imgRailgun, bigBallYellow, 3, 5, 10, projectileList, 3, "left", 50]
    supressor = [True, 150, 1, 500, 0, 50, displayWidth, displayHeight, 100, imgSupressor, bulletYellow, 4, 4, 30, projectileList, 1, "left",30, 0, 10, 1, 0, 2, bigBallRed]
    spyral = [False, 150, 0.5, 500, 0, 50, displayWidth, displayHeight, 100, imgSpyral, carreauGreen, 1, 4, 30, projectileList, 1.5, "left",30, 3]
    miniboss = [False, 500, 0.5, 500, 0, 50, displayWidth, displayHeight, 100, imgMiniBoss, bulletGreen, 1, 4, 90, projectileList, 0.5, "left",150, 3, 1, 3, 10, 3, ballYellow]
    enemyDelayList = [[10, 300, 0], [1870,300,0],[10,300,60],[1870,300,0],[10,300,60],[1870,300,0], [displayWidth/4, 1, 160],[3*displayWidth/4, 1, 0], [0,0,0]]
    enemyList  = [createEnemy(miniBozo), createEnemy(miniBozo), createEnemy(miniBozo),createEnemy(miniBozo), createEnemy(miniBozo), createEnemy(miniBozo), createEnemy(bozo), createEnemy(bozo)]
    # enemyList = []
    onScreenEnemiesList = []
    #create boss
    bossSize = 300
    bossImg = pygame.image.load("img/ships/boss1.png").convert_alpha()
    bossImg = pygame.transform.scale(bossImg, (bossSize, bossSize))
    bossImgAvatar = pygame.image.load("img/avatar/colonelSandersAvatar.png").convert_alpha()
    bossImgAvatar = pygame.transform.scale(bossImgAvatar, (150, 150))
    boss = Boss(10000, 0.5, 0, 0, bossSize, 1920, 1080, 1000, bossImg, projectileList, "Left")
    enemyList.append(boss)
    #onScreenEnemiesList.append(boss)
    bossFight = False

    # Create Button

    buttonSurface = pygame.image.load("img/assets/button.png")
    buttonSurface = pygame.transform.scale(buttonSurface, (buttonSurface.get_width()/1.3, buttonSurface.get_height()/1.3))
    MENU_BUTTON = Button(buttonSurface, 960, 1000, "Main Menu", False, None, None, buttonSurface)


    #Initialize dash coordinates
    timerDash = [0 , 0]

    #Initialize score
    score = Score()

    # Main Loop
    running = True

    # Font importe
    font = pygame.font.Font(None, 36)
    
    # Dialogue phase 1
    textDialogueBossPhase = "Hello mister \nYou're beautiful, I think I love you\nSo I need to beat you to take you\n"
    textDialoguePhase = 0
    textDialoguePhaseBoss = 0
    textDialogue = "Hello,\nI am under the water\nPlease help me\n"
    textDialogueBoss = "\nHello \nSorry lady, I have to many other women\nTry it\n"
    textDialogueSurface = []
    textDialogueSurfaceBoss = []
    space_pressed = False
    
    for line in textDialogue.split('\n'):
        textDialogueSurface.append(get_font(20).render(line, True, "#b68f40"))
        
    for line in textDialogueBoss.split('\n'):
        textDialogueSurfaceBoss.append(get_font(20).render(line, True, "#b68f40"))

    isPaused = False
    isDead = False

    while running:
        oldDamage = boss.health
        # run the game at a constant 60fps
        clock.tick(60)
            
        #Close window on Escape press
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                running=False
            elif events.type == pygame.KEYDOWN:
                if events.key == pygame.K_ESCAPE:
                    isPaused = not isPaused

        # Paused screen
        if isPaused:
            pausedRect = pygame.Surface((1920,1080)) 
            pausedRect.set_alpha(128)               
            pausedRect.fill((0,0,0))           
            screen.blit(pausedRect, (0,0))
            pausedText = get_font(100).render("PAUSED", True, "#b68f40")
            pausedTextRect = pausedText.get_rect(center=(960, 100))
            screen.blit(pausedText,pausedTextRect)
            
            while True:
                MENU_BUTTON.changeColor(pygame.mouse.get_pos(), screen)
                MENU_BUTTON.update(screen)
                event = pygame.event.poll()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if MENU_BUTTON.checkForInput(pygame.mouse.get_pos(), player):
                        running = False
                        isPaused = False
                        break

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        isPaused = False
                        break
                
                pygame.display.flip()
                clock.tick(60)
            continue
            
        if isDead:
            deadRect = pygame.Surface((1920,1080)) 
            deadRect.set_alpha(128)               
            deadRect.fill((0,0,0))           
            screen.blit(deadRect, (0,0))
            deadText = get_font(100).render("GAME OVER", True, "#b68f40")
            deadTextRect = deadText.get_rect(center=(960, 100))
            screen.blit(deadText,deadTextRect)
            deadText = font.render(f'You Lose', True, (255, 255, 255))
            deadTextRect = deadText.get_rect(center=(960, 500))
            screen.blit(deadText, deadTextRect)
            deadText = font.render(f'Score:' + str(score.score), True, (255, 255, 255))
            deadTextRect = deadText.get_rect(center=(960, 550))
            screen.blit(deadText, deadTextRect)
            deadText = font.render(f'Money:' + str(player.money), True, (255, 255, 255))
            deadTextRect = deadText.get_rect(center=(960, 600))
            screen.blit(deadText, deadTextRect)
            
            while True:
                MENU_BUTTON.changeColor(pygame.mouse.get_pos(), screen)
                MENU_BUTTON.update(screen)
                event = pygame.event.poll()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if MENU_BUTTON.checkForInput(pygame.mouse.get_pos(), player):
                        running = False
                        isPaused = False
                        return player.money
                
                pygame.display.flip()
                clock.tick(60)
                
        
        
        # Play music in Loop
        if bossFight:
            backGround = bossBase
            bulletHellSound.stop()
            if bossMusic.get_num_channels() == 0:
                bossMusic.play()
        else:
            backGround = levelBackGround
            if bulletHellSound.get_num_channels() == 0:
                bulletHellSound.play()
        
        #draw scrolling background       
        scroll = int(trueScroll)

        #screen shake
        if shaking:
            scroll += random.randint(0, screenShake) - screenShake/2


        # background scroll
        for i in range(0, tilesHeight):
            for j in range(0, tilesWidth):
                screen.blit(backGround, (j*backGround.get_width(), i*backGround.get_height() - trueScroll))

        
        trueScroll += 1
        # reset scroll
        if trueScroll >= backGround.get_height():
            trueScroll = 0

        # Slow movement and dash
        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_LSHIFT]:
            if pressed[pygame.K_SPACE] and timerDash[1] == 0:
                invincible = True
                timerDash[1] = player.cooldownDash
                timerDash[0] = player.timeDash
                invincibleCountdown = timerDash[0] + 10
                player.speed = player.dashSpeed
            elif timerDash[0] == 0:
                player.speed = player.slowSpeed
        elif pressed[pygame.K_SPACE] and timerDash[1] == 0:
            invincible = True
            timerDash[1] = player.cooldownDash
            timerDash[0] = player.timeDash
            invincibleCountdown = timerDash[0] + player.dashInvulnerability
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
        playerHitbox = pygame.Rect(0,0, player.size/8, player.size/8)
        # center the hitbox on the ship's cockpit
        playerRect = pygame.Rect(player.X+player.size/2 - playerHitbox.width/2, player.Y+player.size/2, playerHitbox.width, playerHitbox.height)
        
        #Add enemies at the right time
        if enemyDelayList != [] and enemyDelayList[0][2] <= 0 and enemyList  != []:
            if enemyList[0] == boss:
                if onScreenEnemiesList == []:
                    transition = True
                    if bossFight:
                        textDialogue = textDialogueBossPhase
                        textDialoguePhase = 0
                        textDialoguePhaseBoss = 0
                        textDialogueSurface = []
                        for line in textDialogue.split('\n'):
                            textDialogueSurface.append(get_font(20).render(line, True, "#b68f40"))
                        onScreenEnemiesList.append(enemyList.pop(0))
                        enemyDelayList.pop(0)
            else:
                
                enemyList[0].x, enemyList[0].y = enemyDelayList[0][0], enemyDelayList[0][1]
                onScreenEnemiesList.append(enemyList.pop(0))
                enemyDelayList.pop(0)

        playerBullets = pygame.surface.Surface((displayWidth, displayHeight))
        enemyBullets = pygame.surface.Surface((displayWidth, displayHeight))

        for bullet in projectileList:
            if bullet.update(onScreenEnemiesList) == True:
                projectileList.pop(projectileList.index(bullet))
            bulletRect = pygame.Rect(bullet.x, bullet.y, bullet.image.get_width(), bullet.image.get_height())
            rotated_image, bulletRect = rotate(bullet.image, bulletRect, bullet.angle)
            screen.blit(rotated_image, (bullet.x, bullet.y))
            if bullet.isPlayer == False:
                playerBullets.blit(rotated_image, (bullet.x, bullet.y))
                #pygame.draw.rect(screen, (255,0,0), bulletRect)
                if playerRect.colliderect(bulletRect) and not invincible:
                    player.getHit()
                    damageAvatarCountdown = 120
                    invincibleCountdown = player.timeInvincible * 60
                    invincible = True
                    projectileList.pop(projectileList.index(bullet))
            else:
                enemyBullets.blit(rotated_image, (bullet.x, bullet.y))
        
        #Enemy
        for enemy in onScreenEnemiesList:
            enemy.update(player)
            if enemy.__class__.__name__ == "Boss":
                bossHitbox = pygame.Rect(0,0, boss.size/2, boss.size)
                # center the hitbox on the boss
                enemyRect = pygame.Rect(boss.x + boss.size/2 - bossHitbox.width/2, boss.y, bossHitbox.width, bossHitbox.height)
            else:
                enemyRect = pygame.Rect(enemy.x, enemy.y, enemy.size, enemy.size)
            #pygame.draw.enemyRect(screen, (255,0,0), enemyRect)
            
            screen.blit(enemy.image, (enemy.x, enemy.y))
            if enemy.y > enemy.displayHeight:
                if enemy.__class__.__name__ == "Boss":
                    boss.move(0,-1)
                else:
                    enemy.health = 0
                    onScreenEnemiesList.pop(onScreenEnemiesList.index(enemy))

            #Collision bullet & enemy
            for bullet in projectileList:
                if bullet.isPlayer == True:
                    bulletRect = pygame.Rect(bullet.x, bullet.y, bullet.size, bullet.size)
                    if enemyRect.colliderect(bulletRect):
                        projectileList.pop(projectileList.index(bullet))
                        enemy.takeDmg(bullet.damage, onScreenEnemiesList, player)
                        score.score_increment(10)
                        
                    if(enemy.health <= 0):
                        score.score_increment(enemy.score)
                        #the enemy pops itself out of onScreenEnemiesList
                        break
            if enemyRect.colliderect(playerRect) and not invincible:
                player.getHit()
                invincibleCountdown = player.timeInvincible * 60
                damageAvatarCountdown = 120
                invincible = True
                if enemy.__class__.__name__ == "Enemy":
                    score.score_increment(10)
                    onScreenEnemiesList.pop(onScreenEnemiesList.index(enemy))
                else:
                    enemy.health -= 10
            enemy.update(player)


        for particle in particleList:
            if(particle.draw(screen, projectileList)):
                particleList.pop(particleList.index(particle))
                shaking = False
            else:
                shaking = True
            
            if(particle.doDamage):
                for enemy in onScreenEnemiesList:
                    enemy.takeDmg(player.ultimateDmg, onScreenEnemiesList, player)

        #Add a bullet to the projectileList list on press
        if pressed[pygame.K_w]:
            player.updateSecondaries()
            if player.cooldown <= 0:
                shift = True
                if player.speed != player.slowSpeed:
                    shift = False
                player.cooldown = player.timeBetweenShots
                player.shoot(shift)
            if player.missileCooldown <= 0 and not shift:
                player.shootHoming()
                player.missileCooldown = player.timeBetweenMissiles
        if pressed[pygame.K_x]:
            if player.ultimateCooldown <= 0:
                #play sfx
                ultimateSound.play()
                player.shootUltimate(particleList)
                player.ultimateCooldown = player.timeBetweenUltimates
        
        player.cooldown -= 1
        player.missileCooldown -= 1
        player.ultimateCooldown -= 1

        if damageAvatarCountdown > 0:
            damageAvatarCountdown -= 1

        if invincibleCountdown > 0:
            invincibleCountdown -= 1
        else: 
            invincible = False

        if enemyDelayList != [] and isPlaying:
            enemyDelayList[0][2] -= 1

        #Score grows automatically
        if pygame.time.get_ticks() - scoreTime >= 3000:
            score.score_increment(30)
            scoreTime = pygame.time.get_ticks()
            
        #Draw player model on screen
        if invincible:
            screen.blit(playerShield, (player.X, player.Y))
        else:
            screen.blit(imgPlayer, (player.X, player.Y))

        screen.blit(playerBullets, (0,0), (0,0,displayWidth, displayHeight), pygame.BLEND_RGB_ADD)
        screen.blit(enemyBullets, (0,0), (0,0,displayWidth, displayHeight), pygame.BLEND_RGB_ADD)
        
        #Write player's score & remaining lives 
        scoreText = font.render(f'Score: {score.score}', True, (255, 255, 255))
        screen.blit(scoreText, (10, 10))
        livesText = font.render(f'Lives: {player.lives}', True, (255, 255, 255))
        screen.blit(livesText, (10, 30))
        ultimateText = font.render(f'Ultimate in: {math.ceil(player.ultimateCooldown/60)}', True, (255, 255, 255))
        screen.blit(ultimateText, (10, 50))
        ultimateText = font.render(f'Money: {player.money}', True, (255, 255, 255))
        screen.blit(ultimateText, (10, 70))
        
        
        # Dialogue phase 1
        textDialogueRect = textDialogueSurface[textDialoguePhase].get_rect(center=(600, 1000))
        if bossFight:
            textDialogueRectBoss = textDialogueSurfaceBoss[textDialoguePhaseBoss].get_rect(center=(1320, 80))
        
        if pressed[pygame.K_SPACE] and textDialoguePhase < len(textDialogueSurface) - 1 and not(space_pressed):
            if bossFight:
                if textDialoguePhaseBoss <= textDialoguePhase:
                    textDialoguePhaseBoss +=1
                else:
                    textDialoguePhase +=1
            else:
                textDialoguePhase +=1
            space_pressed = True
        elif textDialoguePhase >= len(textDialogueSurface) - 1:
            isPlaying = True
            if bossFight:
                textDialoguePhaseBoss = len(textDialogueSurfaceBoss) -1
        if not pressed[pygame.K_SPACE]:
            space_pressed = False
        if textDialoguePhase < len(textDialogueSurface) - 1:
            projectileList.clear()
            invincible = True
            invincibleCountdown = 60


        screen.blit(textDialogueSurface[textDialoguePhase], textDialogueRect)
        if bossFight:
            screen.blit(textDialogueSurfaceBoss[textDialoguePhaseBoss], textDialogueRectBoss)
        
        # Display the hero avatar
        if damageAvatarCountdown > 0:
            screen.blit(imgPlayerAvatarDamage,(0 ,displayHeight - imgPlayerAvatar.get_height()))
        else:
            screen.blit(imgPlayerAvatar,(0 ,displayHeight - imgPlayerAvatar.get_height()))

        # Display the Boss avatar
        if bossFight:
            screen.blit(bossImgAvatar,(displayWidth - bossImgAvatar.get_width() , 0))
        
        currentDamage = boss.health
        deltaD = oldDamage - currentDamage
        deltaText = font.render(f'DPS : {deltaD * 60}', True, (255, 0, 0))
        screen.blit(deltaText, (10, 150))

        bossHPText = font.render(f'Boss HP: {boss.health}', True, (255, 255, 255))
        screen.blit(bossHPText, (10, 100))

        if player.lives == 0:
            bulletHellSound.stop()
            bossMusic.stop()
            post("save.json" ,"money",player.money)
            isDead = True

        if pressed[pygame.K_LSHIFT]:
            pygame.draw.rect(screen, (0,255,0), playerRect)
        
        #transition
        if transition:
            invincible = True
            invincibleCountdown = 5
            if transitionY <= 32:
                drawTransition(transitionSurf, transitionY, (255,255,255))
                new = pygame.transform.scale(transitionSurf, (displayWidth,displayHeight))
                screen.blit(new, (0,0))
                transitionY += 1/6
            elif transitionY > 32:
                bossFight = True
                projectileList.clear()
                if subY <= 32:
                    #the transition surf has a black color key, so drawing in black removes the color
                    drawTransition(transitionSurf, subY, (0,0,0))
                    new = pygame.transform.scale(transitionSurf, (displayWidth,displayHeight))
                    screen.blit(new, (0,0))
                    subY += 1/6
                elif subY >= 32:
                    transition = False
                    transitionY = 0
                    subY = 0
            else:
                transition = False
                transitionY = 0
                subY = 0

        pygame.display.update()
    saveReader(player)
    bossMusic.stop()
    bulletHellSound.stop()
    return player.money
