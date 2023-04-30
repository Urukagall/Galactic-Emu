import pygame
import sys

from Class.button import Button
from Functions.jsonReader import *

playerBlue = pygame.image.load("img/ui/blueSkin.png")
playerBlue = pygame.transform.scale(playerBlue, (200, 75))
playerRed = pygame.image.load("img/ui/redSkin.png")
playerRed = pygame.transform.scale(playerRed, (200, 75))
playerPurple = pygame.image.load("img/ui/purpleSkin.png")
playerPurple = pygame.transform.scale(playerPurple, (200, 75))
playerGreen = pygame.image.load("img/ui/greenSkin.png")
playerGreen = pygame.transform.scale(playerGreen, (200, 75))
buttonSurface = pygame.image.load("img/ui/button.png")
buttonSurface = pygame.transform.scale(buttonSurface, (buttonSurface.get_width()/1.3, buttonSurface.get_height()/1.3))
imgCoin = pygame.image.load("img/ui/coin.png")
imgCoin = pygame.transform.scale(imgCoin, (80, 40))

RESUME_BUTTON = Button(buttonSurface, 960, 850, "Return", False, None, None, buttonSurface)

# Upgrade Button Ship
if get("save.json", "skin") == "playerBlue.png":
    SKIN1_BUTTON = Button(playerBlue, 800, 550, "", True, -1, None, buttonSurface, "A skin")
else:
    SKIN1_BUTTON = Button(playerBlue, 800, 550, "", True, 100, None, buttonSurface, "A skin")
    
if get("save.json", "skin") == "playerRed.png":
    SKIN2_BUTTON = Button(playerRed, 1150, 700, "", True, -1, None, buttonSurface, "A skin")
else:
    SKIN2_BUTTON = Button(playerRed, 1150, 700, "", True, 500, None, buttonSurface, "A skin")
    
if get("save.json", "skin") == "playerPurple.png":
    SKIN3_BUTTON = Button(playerPurple, 1150, 550, "", True, -1, None, buttonSurface, "A skin")
else:
    SKIN3_BUTTON = Button(playerPurple, 1150, 550, "", True, 750, None, buttonSurface, "A skin")
    
if get("save.json", "skin") == "playerGreen.png":
    SKIN4_BUTTON = Button(playerGreen, 800, 700, "", True, -1, None, buttonSurface, "A skin")
else:
    SKIN4_BUTTON = Button(playerGreen, 800, 700, "", True, 1000, None, buttonSurface, "A skin")

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("asset/font.ttf", size)


MENU_TEXT = get_font(100).render("POWER-UP SHOP", True, "#b68f40")
MENU_TEXT_RECT = MENU_TEXT.get_rect(center=(960, 100))

def shopSkin(SCREEN, BG, player, main_menu, gameManager, shop):
    running = True
    while running:
        MENU_MONEY = get_font(20).render(str(player.money), True, "#b68f40")
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.blit(MENU_TEXT, MENU_TEXT_RECT)

        SCREEN.blit(imgCoin,(0 ,50))
        SCREEN.blit(MENU_MONEY, (100,60))
        
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
                    post("save.json", "skin", "playerBlue.png")
                    post("save.json", "skinShield", "playerBlueShield.png")
                    imgPlayer = pygame.image.load("img/ships/playerBlue.png")
                    imgPlayer = pygame.transform.scale(imgPlayer, (50, 50))
                    imgPlayerShield = pygame.image.load("img/ships/playerBlueShield.png")
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
                    post("save.json", "skin", "playerPurple.png")
                    post("save.json", "skinShield", "playerPurpleShield.png")
                    imgPlayer = pygame.image.load("img/ships/playerPurple.png")
                    imgPlayer = pygame.transform.scale(imgPlayer, (50, 50))
                    imgPlayerShield = pygame.image.load("img/ships/playerPurpleShield.png")
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
                    post("save.json", "skin", "playerGreen.png")
                    post("save.json", "skinShield", "playerGreenShield.png")
                    imgPlayer = pygame.image.load("img/ships/playerGreen.png")
                    imgPlayer = pygame.transform.scale(imgPlayer, (50, 50))
                    imgPlayerShield = pygame.image.load("img/ships/playerGreenShield.png")
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
                    post("save.json", "skin", "playerRed.png")
                    post("save.json", "skinShield", "playerRedShield.png")
                    imgPlayer = pygame.image.load("img/ships/playerRed.png")
                    imgPlayer = pygame.transform.scale(imgPlayer, (50, 50))
                    imgPlayerShield = pygame.image.load("img/ships/playerRedShield.png")
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
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    shop(SCREEN, BG, player, main_menu, gameManager)
        pygame.display.update()