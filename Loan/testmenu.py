from Class.button import Button

#Import librairies
import pygame ,sys
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
backGround = pygame.transform.scale(backGround, (100, 100))
backGroundHeight = backGround.get_height()
backGroundWidth = backGround.get_width()

#Pre-requisite for the screen scrolling
trueScroll = 0 
tilesHeight = math.ceil(displayHeight / backGroundHeight) + 1
tilesWidth = math.ceil(displayWidth / backGroundWidth) + 1

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
ultimateSound.set_volume(0.2)

# Import Music

bulletHellSound = pygame.mixer.Sound("sound/Bullet_Hell.mp3")
bulletHellSound.set_volume(0.2)

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

player = Player(10, 5, 50, displayWidth, displayHeight, 30, 60, 15, 5, projectileList, classicBullet, missile)



pygame.init()

SCREEN = pygame.display.set_mode((1920, 1080))
pygame.display.set_caption("Menu")

BG = pygame.image.load("img/Background.png")
BG = pygame.transform.scale(BG,(1920, 1080))

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("img/font.ttf", size)

def play():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")

        PLAY_BACK = Button(image=None, pos=(640, 460), 
                            text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()

        pygame.display.update()
    
def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")

        OPTIONS_TEXT = get_font(45).render("This is the OPTIONS screen.", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(640, 460), 
                            text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()

def quit():
    running = False 
    return running 

imgButton = pygame.image.load("img/button.png")
imgButton = pygame.transform.scale(imgButton, (250,100))
def main_menu():
    running = True
    while running :
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(1000, 100))

        PLAY_BUTTON = Button(imgButton, 1000, 250, "Play", False, 0, play, missile)   
        # text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(imgButton,1000, 400, "Option", False, 0, options,missile )
                            # text_input="OPTIONS", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(imgButton,1000, 550,"Quit", False, 0, quit, missile)
                            # text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS, player):
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS, player):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS, player):
                    running = quit()

        pygame.display.update()

main_menu()