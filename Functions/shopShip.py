import pygame
import sys

from Class.button import Button

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("font.ttf", size)

def shopShip(SCREEN, BG, buttonSurface, player, main_menu, gameManager, shop):
    running = True
    while running:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("SHIP SHOP", True, "#b68f40")
        MENU_TEXT_RECT = MENU_TEXT.get_rect(center=(960, 100))
        MENU_UPGRADE = get_font(30).render("Upgrade", True, "#b68f40")
        MENU_UPGRADE_RECT = MENU_UPGRADE.get_rect(center=(960, 480))

        RESUME_BUTTON = Button(buttonSurface, 960, 400, "Return", False, 0, None, buttonSurface)
        QUIT_BUTTON = Button(buttonSurface, 960, 850, "Quit", False, 0, None, buttonSurface)
        
        
        # Upgrade Button Ship
        LIVE_BUTTON = Button(buttonSurface, 510, 550, "Live", False, 0, None, buttonSurface)
        DASH_BUTTON = Button(buttonSurface, 760, 550, "Dash Cooldown", False, 0, None, buttonSurface)
        SPIRAL_BUTTON = Button(buttonSurface, 510, 700, "Special Spiral", False, 0, None, buttonSurface)
        SPEED_BUTTON = Button(buttonSurface, 760, 700, "Speed", False, 0, None, buttonSurface)
        
        # Upgrade Button bullet
        SPEED_BULLET_BUTTON = Button(buttonSurface, 1160, 550, "Speed", False, 0, None, buttonSurface)
        DAMAGE_BUTTON = Button(buttonSurface, 1410, 550, "Damage", False, 0, None, buttonSurface)
        CANONS_BUTTON = Button(buttonSurface, 1160, 700, "Canons", False, 0, None, buttonSurface)
        FIRERATE_BUTTON = Button(buttonSurface, 1410, 700, "Firerate", False, 0, None, buttonSurface)

        SCREEN.blit(MENU_TEXT, MENU_TEXT_RECT)
        # SCREEN.blit(MENU_UPGRADE, MENU_UPGRADE_RECT)

        for button in [RESUME_BUTTON, LIVE_BUTTON, DASH_BUTTON, SPIRAL_BUTTON, SPEED_BUTTON, SPEED_BULLET_BUTTON, DAMAGE_BUTTON, CANONS_BUTTON, FIRERATE_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS, SCREEN)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if RESUME_BUTTON.checkForInput(MENU_MOUSE_POS, player):
                    shop(SCREEN, BG, buttonSurface, player, main_menu, gameManager)
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS, player):
                    running = False
                    pygame.quit()
                    sys.exit()
        pygame.display.update()