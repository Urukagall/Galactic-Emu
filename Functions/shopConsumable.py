import pygame
import sys

from Class.button import Button
from Functions.jsonReader import *

phoenix = pygame.image.load("img/ui/phoenix.png")
phoenix = pygame.transform.scale(phoenix, (200, 75))
autocanon = pygame.image.load("img/ui/autocanon.png")
autocanon = pygame.transform.scale(autocanon, (200, 75))
shotgun = pygame.image.load("img/ui/shotgun.png")
shotgun = pygame.transform.scale(shotgun, (200, 75))
spiral = pygame.image.load("img/ui/spiral.png")
spiral = pygame.transform.scale(spiral, (200, 75))
buttonSurface = pygame.image.load("img/ui/button.png")
buttonSurface = pygame.transform.scale(buttonSurface, (buttonSurface.get_width()/1.3, buttonSurface.get_height()/1.3))
imgCoin = pygame.image.load("img/ui/coin.png")
imgCoin = pygame.transform.scale(imgCoin, (80, 40))

RESUME_BUTTON = Button(buttonSurface, 960, 850, "Return", False, None, None, buttonSurface)

# Upgrade Button Ship
if get("save.json", "secondaryWeapon1") == "autocanon":
    AUTOCANON_BUTTON = Button(autocanon, 800, 550, "", True, -1, None, buttonSurface, "A high firerate suspended canon")
else:
    AUTOCANON_BUTTON = Button(autocanon, 800, 550, "", True, 100, None, buttonSurface, "A high firerate suspended canon")
    
if get("save.json", "secondaryWeapon2") == "shotgun":
    SHOTGUN_BUTTON = Button(shotgun, 1150, 700, "", True, -1, None, buttonSurface, "Slow firerate but wide angle")
else:
    SHOTGUN_BUTTON = Button(shotgun, 1150, 700, "", True, 150, None, buttonSurface, "Slow firerate but wide angle")
    
if get("save.json", "secondaryWeapon2") == "phoenix":
    PHOENIX_BUTTON = Button(phoenix, 1150, 550, "", True, -1, None, buttonSurface, "A strong and fast missile")
else:
    PHOENIX_BUTTON = Button(phoenix, 1150, 550, "", True, 250, None, buttonSurface, "A strong and fast missile")
    
if get("save.json", "secondaryWeapon1") == "spiral":
    SPIRAL_BUTTON = Button(spiral, 800, 700, "", True, -1, None, buttonSurface, "Shoots bullets all arround your ship")
else:
    SPIRAL_BUTTON = Button(spiral, 800, 700, "", True, 50, None, buttonSurface, "Shoots bullets all arround your ship")

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("asset/font.ttf", size)


MENU_TEXT = get_font(100).render("POWER-UP SHOP", True, "#b68f40")
MENU_TEXT_RECT = MENU_TEXT.get_rect(center=(960, 100))
MENU_SLOT1 = get_font(20).render("Slot 1 :", True, "#b68f40")
MENU_SLOT1_RECT = MENU_SLOT1.get_rect(center=(800, 400))
MENU_SLOT2 = get_font(20).render("Slot 2 :", True, "#b68f40")
MENU_SLOT2_RECT = MENU_SLOT2.get_rect(center=(1150, 400))

def shopConsumable(SCREEN, BG, player, main_menu, gameManager, shop):
    running = True
    while running:
        MENU_MONEY = get_font(20).render(str(player.money), True, "#b68f40")
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.blit(MENU_TEXT, MENU_TEXT_RECT)
        SCREEN.blit(MENU_SLOT1, MENU_SLOT1_RECT)
        SCREEN.blit(MENU_SLOT2, MENU_SLOT2_RECT)

        SCREEN.blit(imgCoin,(0 ,50))
        SCREEN.blit(MENU_MONEY, (100,60))
        
        for button in [RESUME_BUTTON, SHOTGUN_BUTTON, PHOENIX_BUTTON, SPIRAL_BUTTON, AUTOCANON_BUTTON]:
            button.changeColor(MENU_MOUSE_POS, SCREEN)
            button.update(SCREEN)
            
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if RESUME_BUTTON.checkForInput(MENU_MOUSE_POS, player):
                    shop(SCREEN, BG, player, main_menu, gameManager)
                if AUTOCANON_BUTTON.checkForInput(MENU_MOUSE_POS, player):
                    post("save.json", "secondaryWeapon1", "autocanon")
                    player.secondaryWeapon1 = "autocanon"
                    AUTOCANON_BUTTON.price = -1
                    if SPIRAL_BUTTON.price == -1:
                        SPIRAL_BUTTON.price = 50
                        SPIRAL_BUTTON.isLevelMax = False
                elif SHOTGUN_BUTTON.checkForInput(MENU_MOUSE_POS, player):
                    post("save.json", "secondaryWeapon2", "shotgun")
                    player.secondaryWeapon2 = "shotgun"
                    SHOTGUN_BUTTON.price = -1
                    if PHOENIX_BUTTON.price == -1:
                        PHOENIX_BUTTON.price = 250
                        PHOENIX_BUTTON.isLevelMax = False
                elif PHOENIX_BUTTON.checkForInput(MENU_MOUSE_POS, player):
                    post("save.json", "secondaryWeapon2", "phoenix")
                    player.secondaryWeapon2 = "phoenix"
                    PHOENIX_BUTTON.price = -1
                    if SHOTGUN_BUTTON.price == -1:
                        SHOTGUN_BUTTON.price = 150
                        SHOTGUN_BUTTON.isLevelMax = False
                elif SPIRAL_BUTTON.checkForInput(MENU_MOUSE_POS, player):
                    post("save.json", "secondaryWeapon1", "spiral")
                    player.secondaryWeapon1 = "spiral"
                    SPIRAL_BUTTON.price = -1
                    if AUTOCANON_BUTTON.price == -1:
                        AUTOCANON_BUTTON.price = 100
                        AUTOCANON_BUTTON.isLevelMax = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    shop(SCREEN, BG, player, main_menu, gameManager)
        pygame.display.update()