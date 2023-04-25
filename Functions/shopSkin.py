import pygame
import sys

from Class.button import Button
from Functions.jsonReader import *

phoenix = pygame.image.load("img/assets/buttonAmelioration/phoenix.png")
phoenix = pygame.transform.scale(phoenix, (200, 75))
buttonSurface = pygame.image.load("img/assets/button.png")
buttonSurface = pygame.transform.scale(buttonSurface, (buttonSurface.get_width()/1.3, buttonSurface.get_height()/1.3))

RESUME_BUTTON = Button(buttonSurface, 960, 850, "Return", False, None, None, buttonSurface)

# Upgrade Button Ship
if get("save.json", "skin") == "player":
    SKIN1_BUTTON = Button(buttonSurface, 800, 550, "", True, -1, None, buttonSurface, "A skin")
else:
    SKIN1_BUTTON = Button(buttonSurface, 800, 550, "", True, 100, None, buttonSurface, "A skin")
    
if get("save.json", "skin") == "shotgun":
    SKIN2_BUTTON = Button(buttonSurface, 1150, 700, "", True, -1, None, buttonSurface, "A skin")
else:
    SKIN2_BUTTON = Button(buttonSurface, 1150, 700, "", True, 500, None, buttonSurface, "A skin")
    
if get("save.json", "skin") == "phoenix":
    SKIN3_BUTTON = Button(phoenix, 1150, 550, "", True, -1, None, buttonSurface, "A skin")
else:
    SKIN3_BUTTON = Button(phoenix, 1150, 550, "", True, 750, None, buttonSurface, "A skin")
    
if get("save.json", "skin") == "spiral":
    SKIN4_BUTTON = Button(buttonSurface, 800, 700, "", True, -1, None, buttonSurface, "A skin")
else:
    SKIN4_BUTTON = Button(buttonSurface, 800, 700, "", True, 1000, None, buttonSurface, "A skin")
    
# SHOTGUN_BUTTON = Button(buttonSurface, 800, 700, "Shotgun", True, 150, None, buttonSurface, "Slow firerate but wide angle")
# PHOENIX_BUTTON = Button(buttonSurface, 1150, 550, "Phoenix", True, 250, None, buttonSurface, "A strong and fast missile")
# SPIRAL_BUTTON = Button(buttonSurface, 1150, 700, "Spiral", True, 50, None, buttonSurface, "Shoots bullets all arround your ship")

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("font.ttf", size)


MENU_TEXT = get_font(100).render("POWER-UP SHOP", True, "#b68f40")
MENU_TEXT_RECT = MENU_TEXT.get_rect(center=(960, 100))
MENU_SLOT1 = get_font(20).render("Slot 1 :", True, "#b68f40")
MENU_SLOT1_RECT = MENU_SLOT1.get_rect(center=(800, 400))
MENU_SLOT2 = get_font(20).render("Slot 2 :", True, "#b68f40")
MENU_SLOT2_RECT = MENU_SLOT2.get_rect(center=(1150, 400))

def shopSkin(SCREEN, BG, player, main_menu, gameManager, shop):
    running = True
    while running:
        MENU_MONEY = get_font(20).render("Money:" + str(player.money), True, "#b68f40")
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.blit(MENU_TEXT, MENU_TEXT_RECT)
        SCREEN.blit(MENU_SLOT1, MENU_SLOT1_RECT)
        SCREEN.blit(MENU_SLOT2, MENU_SLOT2_RECT)

        SCREEN.blit(MENU_MONEY, (50,50))
        
        for button in [RESUME_BUTTON, SKIN1_BUTTON, SKIN2_BUTTON, SKIN3_BUTTON, SKIN4_BUTTON]:
            button.changeColor(MENU_MOUSE_POS, SCREEN)
            button.update(SCREEN)
            
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if RESUME_BUTTON.checkForInput(MENU_MOUSE_POS, player):
                    shop(SCREEN, BG, player, main_menu, gameManager)
                if SKIN1_BUTTON.checkForInput(MENU_MOUSE_POS, player):
                    post("save.json", "skin", "emeu.jpg")
                    post("save.json", "skinShield", "enemy.png")
                    imgPlayer = pygame.image.load("img/ships/emeu.jpg")
                    imgPlayer = pygame.transform.scale(imgPlayer, (50, 50))
                    imgPlayerShield = pygame.image.load("img/ships/enemy.png")
                    imgPlayerShield = pygame.transform.scale(imgPlayerShield, (50, 50))
                    player.img = imgPlayer
                    player.imgShield = imgPlayerShield
                    SKIN1_BUTTON.price = -1

                    SKIN2_BUTTON.price = 500
                    SKIN2_BUTTON.isLevelMax = False
                    SKIN3_BUTTON.price = 750
                    SKIN3_BUTTON.isLevelMax = False
                    SKIN4_BUTTON.price = 1000
                    SKIN4_BUTTON.isLevelMax = False
                elif SKIN3_BUTTON.checkForInput(MENU_MOUSE_POS, player):
                    post("save.json", "skin", "emeu.jpg")
                    post("save.json", "skinShield", "enemy.png")
                    imgPlayer = pygame.image.load("img/ships/emeu.jpg")
                    imgPlayer = pygame.transform.scale(imgPlayer, (50, 50))
                    imgPlayerShield = pygame.image.load("img/ships/enemy.png")
                    imgPlayerShield = pygame.transform.scale(imgPlayerShield, (50, 50))
                    player.img = imgPlayer
                    player.imgShield = imgPlayerShield
                    SKIN3_BUTTON.price = -1
                    
                    SKIN2_BUTTON.price = 500
                    SKIN2_BUTTON.isLevelMax = False
                    SKIN1_BUTTON.price = 50
                    SKIN1_BUTTON.isLevelMax = False
                    SKIN4_BUTTON.price = 1000
                    SKIN4_BUTTON.isLevelMax = False
                elif SKIN4_BUTTON.checkForInput(MENU_MOUSE_POS, player):
                    post("save.json", "skin", "emeu.jpg")
                    post("save.json", "skinShield", "enemy.png")
                    imgPlayer = pygame.image.load("img/ships/emeu.jpg")
                    imgPlayer = pygame.transform.scale(imgPlayer, (50, 50))
                    imgPlayerShield = pygame.image.load("img/ships/enemy.png")
                    imgPlayerShield = pygame.transform.scale(imgPlayerShield, (50, 50))
                    player.img = imgPlayer
                    player.imgShield = imgPlayerShield
                    SKIN4_BUTTON.price = -1
                    
                    SKIN2_BUTTON.price = 500
                    SKIN2_BUTTON.isLevelMax = False
                    SKIN3_BUTTON.price = 750
                    SKIN3_BUTTON.isLevelMax = False
                    SKIN1_BUTTON.price = 50
                    SKIN1_BUTTON.isLevelMax = False
                elif SKIN2_BUTTON.checkForInput(MENU_MOUSE_POS, player):
                    post("save.json", "skin", "emeu.jpg")
                    post("save.json", "skinShield", "enemy.png")
                    imgPlayer = pygame.image.load("img/ships/emeu.jpg")
                    imgPlayer = pygame.transform.scale(imgPlayer, (50, 50))
                    imgPlayerShield = pygame.image.load("img/ships/enemy.png")
                    imgPlayerShield = pygame.transform.scale(imgPlayerShield, (50, 50))
                    player.img = imgPlayer
                    player.imgShield = imgPlayerShield
                    SKIN2_BUTTON.price = -1
                    
                    SKIN1_BUTTON.price = 50
                    SKIN1_BUTTON.isLevelMax = False
                    SKIN3_BUTTON.price = 750
                    SKIN3_BUTTON.isLevelMax = False
                    SKIN4_BUTTON.price = 1000
                    SKIN4_BUTTON.isLevelMax = False
        pygame.display.update()