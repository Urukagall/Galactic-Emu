import pygame
import sys

from Class.button import Button

from Functions.jsonReader import *

buttonSurface = pygame.image.load("img/assets/button.png")
buttonSurface = pygame.transform.scale(buttonSurface, (buttonSurface.get_width()/1.3, buttonSurface.get_height()/1.3))

RESUME_BUTTON = Button(buttonSurface, 960, 850, "Return", False, None, None, buttonSurface)

# Upgrade Button Bullet 1
SPEED_BULLET_BUTTON = Button(buttonSurface, 510, 550, "Speed", True, get("Upgrade.json", "bulletSpeedPrice1")[get("Upgrade.json", "bulletSpeedLevel1")], None, buttonSurface, "Increase the speed of the bullet")
DAMAGE_BUTTON = Button(buttonSurface, 760, 550, "Damage", True, 10, None, buttonSurface, "Increase the damage of the bullet")
CANONS_BUTTON = Button(buttonSurface, 510, 700, "Canons", True, 20, None, buttonSurface, "Shoot more bullet")
FIRERATE_BUTTON = Button(buttonSurface, 760, 700, "Firerate", True, 30, None, buttonSurface, "Increase the firerate of the bullet")

# Upgrade Button bullet 2
SPEED_BULLET_2_BUTTON = Button(buttonSurface, 1160, 550, "Speed", True, 10, None, buttonSurface, "Increase the speed of the bullet")
DAMAGE_2_BUTTON = Button(buttonSurface, 1410, 550, "Damage", True, 10, None, buttonSurface, "Increase the damage of the bullet")
CANONS_2_BUTTON = Button(buttonSurface, 1160, 700, "Canons", True, 20, None, buttonSurface, "Shoot more bullet")
FIRERATE_2_BUTTON = Button(buttonSurface, 1410, 700, "Firerate", True, 30, None, buttonSurface, "Increase the firerate of the bullet")

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("font.ttf", size)

MENU_TEXT = get_font(100).render("BULLET SHOP", True, "#b68f40")
MENU_TEXT_RECT = MENU_TEXT.get_rect(center=(960, 100))
MENU_UPGRADE_1 = get_font(30).render("Bullet 1", True, "#b68f40")
MENU_UPGRADE_1_RECT = MENU_UPGRADE_1.get_rect(center=(640, 430))

MENU_UPGRADE_2 = get_font(30).render("Bullet 2", True, "#b68f40")
MENU_UPGRADE_2_RECT = MENU_UPGRADE_2.get_rect(center=(1290, 430))

def shopBullet(SCREEN, BG, player, main_menu, gameManager, shop):
    running = True
    while running:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.blit(MENU_TEXT, MENU_TEXT_RECT)
        SCREEN.blit(MENU_UPGRADE_1, MENU_UPGRADE_1_RECT)
        SCREEN.blit(MENU_UPGRADE_2, MENU_UPGRADE_2_RECT)
        for button in [RESUME_BUTTON, SPEED_BULLET_2_BUTTON, DAMAGE_2_BUTTON, CANONS_2_BUTTON, FIRERATE_2_BUTTON, SPEED_BULLET_BUTTON, DAMAGE_BUTTON, CANONS_BUTTON, FIRERATE_BUTTON]:
            button.changeColor(MENU_MOUSE_POS, SCREEN)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if RESUME_BUTTON.checkForInput(MENU_MOUSE_POS, player):
                    shop(SCREEN, BG, player, main_menu, gameManager)
                if SPEED_BULLET_BUTTON.checkForInput(MENU_MOUSE_POS, player):
                    post("Upgrade.json" ,"bulletSpeedLevel1" ,get("Upgrade.json" ,"bulletSpeedLevel1")+1)
                    SPEED_BULLET_BUTTON.price = get("Upgrade.json", "bulletSpeedPrice1")[get("Upgrade.json", "bulletSpeedLevel1")]
                if DAMAGE_BUTTON.checkForInput(MENU_MOUSE_POS, player):
                    print("faut mettre un truc")
                if CANONS_BUTTON.checkForInput(MENU_MOUSE_POS, player):
                    print("faut mettre un truc")
                if FIRERATE_BUTTON.checkForInput(MENU_MOUSE_POS, player):
                    print("faut mettre un truc")
                if SPEED_BULLET_2_BUTTON.checkForInput(MENU_MOUSE_POS, player):
                    print("faut mettre un truc")
                if DAMAGE_2_BUTTON.checkForInput(MENU_MOUSE_POS, player):
                    print("faut mettre un truc")
                if CANONS_2_BUTTON.checkForInput(MENU_MOUSE_POS, player):
                    print("faut mettre un truc")
                if FIRERATE_2_BUTTON.checkForInput(MENU_MOUSE_POS, player):
                    print("faut mettre un truc")
        pygame.display.update()