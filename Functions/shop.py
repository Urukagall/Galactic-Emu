import pygame
import sys
from Class.button import Button
from Functions.shopBullet import shopBullet
from Functions.shopConsumable import shopConsumable
from Functions.shopShip import shopShip


buttonSurface = pygame.image.load("img/assets/button.png")
buttonSurface = pygame.transform.scale(buttonSurface, (buttonSurface.get_width()/1.3, buttonSurface.get_height()/1.3))

RESUME_BUTTON = Button(buttonSurface, 960, 700, "Return", False, None, None, buttonSurface)

# Upgrade Button Ship
SHIP_BUTTON = Button(buttonSurface, 660, 550, "Ship Upgrade", False, None, None, buttonSurface)

# Consumable Button
CONSUMABLE_BUTTON = Button(buttonSurface, 960, 550, "Consumable", False, None, None, buttonSurface)

# Upgrade Button bullet
BULLET_BUTTON = Button(buttonSurface, 1260, 550, "Bullet Upgrade", False, None, None, buttonSurface)

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("font.ttf", size)

MENU_TEXT = get_font(100).render("SHOP", True, "#b68f40")
MENU_TEXT_RECT = MENU_TEXT.get_rect(center=(960, 100))
MENU_UPGRADE = get_font(30).render("Upgrade", True, "#b68f40")
MENU_UPGRADE_RECT = MENU_UPGRADE.get_rect(center=(960, 480))

def shop(SCREEN, BG, player, main_menu, gameManager):
    running = True
    while running:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()



        SCREEN.blit(MENU_TEXT, MENU_TEXT_RECT)
        # SCREEN.blit(MENU_UPGRADE, MENU_UPGRADE_RECT)
        for button in [RESUME_BUTTON, SHIP_BUTTON, BULLET_BUTTON, CONSUMABLE_BUTTON]:
            button.changeColor(MENU_MOUSE_POS, SCREEN)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if RESUME_BUTTON.checkForInput(MENU_MOUSE_POS, player):
                    main_menu()
                if SHIP_BUTTON.checkForInput(MENU_MOUSE_POS, player):
                    shopShip(SCREEN, BG, player, main_menu, gameManager, shop)
                if CONSUMABLE_BUTTON.checkForInput(MENU_MOUSE_POS, player):
                    shopConsumable(SCREEN, BG, player, main_menu, gameManager, shop)
                if BULLET_BUTTON.checkForInput(MENU_MOUSE_POS, player):
                    shopBullet(SCREEN, BG, player, main_menu, gameManager, shop)
        pygame.display.update()