import pygame
import sys

from Class.button import Button
from Functions.jsonReader import *

buttonSurface = pygame.image.load("img/assets/button.png")
buttonSurface = pygame.transform.scale(buttonSurface, (buttonSurface.get_width()/1.3, buttonSurface.get_height()/1.3))

RESUME_BUTTON = Button(buttonSurface, 960, 850, "Return", False, None, None, buttonSurface)

# Upgrade Button Ship
AUTOCANON_BUTTON = Button(buttonSurface, 510, 550, "Autocanon", True, 100, None, buttonSurface, "A high firerate suspended canon")
SHOTGUN_BUTTON = Button(buttonSurface, 760, 550, "Shotgun", True, 150, None, buttonSurface, "Slow firerate but wide angle")
PHOENIX_BUTTON = Button(buttonSurface, 510, 700, "Phoenix", True, 250, None, buttonSurface, "A strong and fast missile")
SPEED_BUTTON = Button(buttonSurface, 760, 700, "Speed", False, None, None, buttonSurface)

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("font.ttf", size)


MENU_TEXT = get_font(100).render("CONSUMABLE SHOP", True, "#b68f40")
MENU_TEXT_RECT = MENU_TEXT.get_rect(center=(960, 100))
MENU_UPGRADE = get_font(30).render("Upgrade", True, "#b68f40")
MENU_UPGRADE_RECT = MENU_UPGRADE.get_rect(center=(960, 480))

def shopConsumable(SCREEN, BG, player, main_menu, gameManager, shop):
    running = True
    while running:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.blit(MENU_TEXT, MENU_TEXT_RECT)
        # SCREEN.blit(MENU_UPGRADE, MENU_UPGRADE_RECT)

        for button in [RESUME_BUTTON, SHOTGUN_BUTTON, PHOENIX_BUTTON, SPEED_BUTTON, AUTOCANON_BUTTON]:
            button.changeColor(MENU_MOUSE_POS, SCREEN)
            button.update(SCREEN)
            if AUTOCANON_BUTTON.checkForInput(MENU_MOUSE_POS, player):
                post("save.json", "secondaryWeapon1", "autocanon")
            elif SHOTGUN_BUTTON.checkForInput(MENU_MOUSE_POS, player):
                post("save.json", "secondaryWeapon2", "shotgun")
            elif PHOENIX_BUTTON.checkForInput(MENU_MOUSE_POS, player):
                post("save.json", "secondaryWeapon2", "phoenix")
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if RESUME_BUTTON.checkForInput(MENU_MOUSE_POS, player):
                    shop(SCREEN, BG, player, main_menu, gameManager)
        pygame.display.update()