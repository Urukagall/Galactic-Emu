#Import librairies
import pygame, sys
import pygame.time

#Import Classes
from Class.player import Player
from Class.button import Button
from Class.gameManager import GameManager

#Import Patterns
from Functions.enemiesPattern import *
from Functions.options import gameOptions
from Functions.shop import shop
from Functions.play import *


buttonSurface = pygame.image.load("img/button.png")
buttonSurface = pygame.transform.scale(buttonSurface, (200, 75))

#Import missile model
missile = pygame.image.load("img/missile.png")
missile = pygame.transform.scale(missile, (missile.get_width(), missile.get_height()))
missileWidth = missile.get_width()

#Import bullets 
classicBullet =  pygame.image.load("img/bullet.png")
classicBullet = pygame.transform.scale(classicBullet, (classicBullet.get_width()*2, classicBullet.get_height()*2))
carreauBlue =  pygame.image.load("img/carreau.png")
carreauBlue = pygame.transform.scale(carreauBlue, (carreauBlue.get_width()*2, carreauBlue.get_height()*2))

#projectileList & CD
projectileList = []

imgPlayer = pygame.image.load("img/player.png")
imgPlayer = pygame.transform.scale(imgPlayer, (50, 50))

player = Player(10, 5, 50, 1920, 1080, 30, 60, 15, 5, projectileList, classicBullet, missile, carreauBlue)

SCREEN = pygame.display.set_mode((1920, 1080))
pygame.display.set_caption("Menu")  

BG = pygame.image.load("img/background.png")
BG = pygame.transform.scale(BG, (1920, 1080))

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("font.ttf", size)

gameManager = GameManager()

def main_menu():
    running = True
    while running:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(960, 100))

        PLAY_BUTTON = Button(buttonSurface, 960, 400, "Play", False, 0, play, buttonSurface)
        SHOP_BUTTON = Button(buttonSurface, 960, 550, "Shop", False, 0, gameOptions, buttonSurface)
        OPTIONS_BUTTON = Button(buttonSurface, 960, 700, "Options", False, 0, gameOptions, buttonSurface)
        QUIT_BUTTON = Button(buttonSurface, 960, 850, "Quit", False, 0, None, buttonSurface)

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, SHOP_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS, SCREEN)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS, player):
                    play(missile, classicBullet, projectileList, player, gameManager)
                if SHOP_BUTTON.checkForInput(MENU_MOUSE_POS, player):
                    shop(SCREEN, BG, buttonSurface, player, main_menu, gameManager)
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS, player):
                    gameOptions(SCREEN, BG, buttonSurface, player, main_menu, gameManager)
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS, player):
                    running = False
                    pygame.quit()
                    sys.exit()
        pygame.display.update()
        
main_menu()