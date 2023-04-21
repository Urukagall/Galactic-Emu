import pygame, sys
import math
import pygame.time
import random

from Class.projectile import Projectile
from Class.player import Player
from Class.enemy import Enemy
from Class.score import Score
from Class.button import Button
from Class.boss import Boss

from Functions.enemiesPattern import *
from Functions.transition import *

def drawTransition(surf, y, color):
    for x in range(16):
        pygame.draw.rect(surf, color, (x, 16 - y, 1, y))
        y -= 1

def darken(image, percent = 50):
    '''Creates a  darkened copy of an image, darkened by percent (50% by default)'''
    newImg = image.copy()
    dark = pygame.Surface(newImg.get_size()).convert_alpha()
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

def play(statsPlayer, gameManager):
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
    bossBase = pygame.transform.scale(bossBase, (2140, 2140))
    bossBaseCoordinates = pygame.Vector2(0,0)
    bossBaseFacing = "right"

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
    missileCooldown = 0
    bulletCoolDown = 0
    ultimateCooldown = 0
    scoreTime = 0

    particleList = []
    shaking = False
    screenShake = 40

    #Redefine player & its bullets luminosity
    imgPlayer = pygame.image.load("img/ships/player.png").convert_alpha()
    imgPlayer = pygame.transform.scale(imgPlayer, (50, 50))
    playerShield = pygame.image.load("img/ships/playerShield.png").convert_alpha()
    playerShield = pygame.transform.scale(playerShield, (50, 50))
    invincible = False
    timeInvincible = 0 #in seconds
    invincibleCountdown = 0

    darkCarreau = darken(carreauBlue)
    darkBullet = darken(bulletBlue)
    darkMissile = darken(missileBlue)

    player = Player(10, 5, 50, 1920, 1080, 30, 60, 15, 5, projectileList, bulletBlue, missileBlue, carreauBlue)

    #Load different images for enemies
    imgRailgun = pygame.image.load("img/ships/railgun.png").convert_alpha()
    imgRailgun = pygame.transform.scale(imgRailgun, (50, 50))
    imgBozo = pygame.image.load("img/ships/bozo.png").convert_alpha()
    imgBozo = pygame.transform.scale(imgBozo, (50, 50))
    imgSupressor = pygame.image.load("img/ships/supressor.png").convert_alpha()
    imgSupressor = pygame.transform.scale(imgSupressor, (50,50))
    imgSpyral = pygame.image.load("img/ships/spyral.png").convert_alpha()
    imgSpyral = pygame.transform.scale(imgSpyral, (50,50))
    imgMiniBoss = pygame.image.load("img/ships/mini_boss.png").convert_alpha()
    imgMiniBoss = pygame.transform.scale(imgMiniBoss, (50,50))

    #Create Enemy
    enemyDelayList = [[0, 0, 50], [0, 0, 100], [0, 0, 50], [0, 0, 100], [0, 0, 100], [0, 0, 100], [0, 0, 100], [0, 0, 100]]
    bozo = Enemy(True, 100, 2, 1200, 0, 50, displayWidth, displayHeight, 100, imgBozo, bulletRed, 10, 1, 0, projectileList, 1, "left")
    railgun = Enemy(True, 300, 0.5, 300, 0, 50, displayWidth, displayHeight, 100, imgRailgun, bigBallYellow, 3, 5, 10, projectileList, 3, "left")
    supressor = Enemy(True, 150, 1, 500, 0, 50, displayWidth, displayHeight, 100, imgSupressor, bulletYellow, 4, 4, 30, projectileList, 1, "left", 0, 10, 1, 0, 2, bigBallRed)
    spyral = Enemy(False, 150, 0.5, 500, 0, 50, displayWidth, displayHeight, 100, imgSpyral, carreauGreen, 1, 4, 30, projectileList, 1.5, "left", 3)
    miniboss = Enemy(False, 500, 0.5, 500, 0, 50, displayWidth, displayHeight, 100, imgMiniBoss, bulletGreen, 1, 4, 90, projectileList, 0.5, "left", 3, 1, 3, 10, 3, ballYellow)
    enemyList  = [bozo, railgun, bozo, spyral, bozo, supressor, miniboss]
    #enemyList = []
    onScreenEnemiesList = []

    #create boss
    bossSize = 300
    bossImg = pygame.image.load("img/ships/boss1.png").convert_alpha()
    bossImg = pygame.transform.scale(bossImg, (bossSize, bossSize))
    boss = Boss(10000, 1, 0, 0, bossSize, 1920, 1080, 1000, bossImg, projectileList, "Left")
    #onScreenEnemiesList.append(boss)
    bossFight = False

    # Create Button
    button_surface = pygame.image.load("img/assets/button.png").convert_alpha()
    button_surface = pygame.transform.scale(button_surface, (200, 75))

    button = Button(button_surface, 500, 500, "Change Weapon price:30", True, 30, Button.ChangeWeapon, imgBozo)
    button2 = Button(button_surface, 900, 700, "Do nothing", False, 0, Button.ChangeWeapon, None)

    buttonList = [button, button2]

    #Initialize dash coordinates
    timerDash = [0 , 0]

    #Initialize score
    score = Score()

    # Main Loop
    running = True

    # Font importe
    font = pygame.font.Font(None, 36)

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
                    running=False
        # Play music in Loop
        
        if bossFight:
            transition = True
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
            
        for i in range(0, tilesHeight):
            for j in range(0, tilesWidth):
                screen.blit(backGround, (j*backGround.get_width(), i*backGround.get_height() - trueScroll))

        if bossFight:
            screen.blit(bossBase, bossBaseCoordinates)
            if bossBaseCoordinates.x < -3*bossBase.get_width()/4:
                bossBaseFacing = "right"
            elif bossBaseCoordinates.x > displayWidth - bossBase.get_width()/4:
                bossBaseFacing = "left"

            if bossBaseFacing == "right":
                bossBaseCoordinates.x += 1
            else:
                bossBaseCoordinates.x -= 1

            if bossBaseCoordinates.y < -3*bossBase.get_height()/4:
                bossBaseFacing = "down"
            elif bossBaseCoordinates.y > displayHeight - bossBase.get_height()/4:
                bossBaseFacing = "up"

            if bossBaseFacing == "down":
                bossBaseCoordinates.y += 1
            else:
                bossBaseCoordinates.y -= 1
        
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
            invincibleCountdown = timerDash[0] + 10
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
                bossFight = True
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
                    invincibleCountdown = timeInvincible * 60
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
                        enemy.takeDmg(bullet.damage, onScreenEnemiesList)
                        score.score_increment(10)
                        
                    if(enemy.health <= 0):
                        player.money += 10
                        score.score_increment(enemy.score)
                        #the enemy pops itself out of onScreenEnemiesList
                        break
            if enemyRect.colliderect(playerRect):
                if not invincible:
                    player.getHit()
                    invincibleCountdown = timeInvincible * 60
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
                    enemy.takeDmg(player.ultimateDmg, onScreenEnemiesList)

        #Add a bullet to the projectileList list on press
        if pressed[pygame.K_w]:
            if player.cooldown <= 0:
                shift = True
                if player.speed != player.slowSpeed:
                    shift = False
                    if player.missileCooldown <= 0:
                        player.shootHoming()
                        player.missileCooldown = player.timeBetweenMissiles
                player.cooldown = player.timeBetweenShots
                player.shoot(shift)
        if pressed[pygame.K_x]:
            if player.ultimateCooldown <= 0:
                #play sfx
                ultimateSound.play()
                player.shootUltimate(particleList)
                player.ultimateCooldown = player.timeBetweenUltimates
        
        player.cooldown -= 1
        player.missileCooldown -= 1
        player.ultimateCooldown -= 1

        if invincibleCountdown > 0:
            invincibleCountdown -= 1
        else: 
            invincible = False

        if enemyDelayList != []:
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

        currentDamage = boss.health
        deltaD = oldDamage - currentDamage
        deltaText = font.render(f'DPS : {deltaD * 60}', True, (255, 0, 0))
        screen.blit(deltaText, (10, 150))

        bossHPText = font.render(f'Boss HP: {boss.health}', True, (255, 255, 255))
        screen.blit(bossHPText, (10, 100))

        if player.lives == 0:
            loseMainText = font.render(f'You died... how unfortunate,', True, (255, 255, 255))
            screen.blit(loseMainText, (800, 500))
            loseMinText = font.render(f'stats back to default ones.', True, (255, 255, 255))
            screen.blit(loseMinText, (800, 550))
            return player.money

        if pressed[pygame.K_LSHIFT]:
            pygame.draw.rect(screen, (0,255,0), playerRect)

        #Transition
        if transition:
            if transitionY <= 32:
                drawTransition(transitionSurf, transitionY, (255,255,255))
                new = pygame.transform.scale(transitionSurf, (displayWidth, displayHeight))
                screen.blit(new, (0,0))
                transitionY += 1/6
        elif transitionY > 32:
            if subY <= 32:
                drawTransition(transitionSurf, subY, (0,0,0))
                new = pygame.transform.scale(transitionSurf, (displayWidth, displayHeight))
                screen.blit(new, (0,0))
                subY += 1/6

        pygame.display.update()
    bossMusic.stop()
