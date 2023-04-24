import pygame
import sys

from Class.button import Button
from Functions.jsonReader import *


buttonSurface = pygame.image.load("img/assets/button.png")
buttonSurface = pygame.transform.scale(buttonSurface, (buttonSurface.get_width()/1.3, buttonSurface.get_height()/1.3))
bulletNumberUp = pygame.image.load("img/assets/buttonAmelioration/bullet_number_up.png")
bulletNumberUp = pygame.transform.scale(bulletNumberUp, (bulletNumberUp.get_width()/3, bulletNumberUp.get_height()/3))
bulletSpeedUp = pygame.image.load("img/assets/buttonAmelioration/bullet_speed_up.png")
bulletSpeedUp = pygame.transform.scale(bulletSpeedUp, (bulletSpeedUp.get_width()/1.3, bulletSpeedUp.get_height()/1.3))
bulletFirerateUp = pygame.image.load("img/assets/buttonAmelioration/fire_rate_up.png")
bulletFirerateUp = pygame.transform.scale(bulletFirerateUp, (bulletFirerateUp.get_width()/1.3, bulletFirerateUp.get_height()/1.3))

RESUME_BUTTON = Button(buttonSurface, 960, 850, "Return", False, None, None, buttonSurface)

# Upgrade Button Bullet 1
SPEED_BULLET_BUTTON = Button(buttonSurface, 510, 550, "Speed", True, get("upgrade.json", "bulletSpeedPrice")[get("upgrade.json", "bulletSpeedLevel")], None, buttonSurface, "Increase the speed of the bullet")
DAMAGE_BULLET_BUTTON = Button(buttonSurface, 760, 550, "Damage", True, get("upgrade.json", "bulletDamagePrice")[get("upgrade.json", "bulletDamageLevel")], None, buttonSurface, "Increase the damage of the bullet")
CANONS_BULLET_BUTTON = Button(buttonSurface, 510, 700, "Canons", True, get("upgrade.json", "bulletCanonsPrice")[get("upgrade.json", "bulletCanonsLevel")], None, buttonSurface, "Shoot more bullet")
FIRERATE_BULLET_BUTTON = Button(buttonSurface, 760, 700, "Firerate", True, get("upgrade.json", "bulletFireratePrice")[get("upgrade.json", "bulletFirerateLevel")], None, buttonSurface, "Increase the firerate of the bullet")

# Upgrade Button bullet 2
SPEED_MISSILE_BUTTON = Button(buttonSurface, 1160, 550, "Speed", True, get("upgrade.json", "missileSpeedPrice")[get("upgrade.json", "missileSpeedLevel")], None, buttonSurface, "Increase the speed of the bullet")
DAMAGE_MISSILE_BUTTON = Button(buttonSurface, 1410, 550, "Damage", True, get("upgrade.json", "missileDamagePrice")[get("upgrade.json", "missileDamageLevel")], None, buttonSurface, "Increase the damage of the bullet")
CANONS_MISSILE_BUTTON = Button(buttonSurface, 1160, 700, "Canons", True, get("upgrade.json", "missileCanonsPrice")[get("upgrade.json", "missileCanonsLevel")], None, buttonSurface, "Shoot more bullet")
FIRERATE_MISSILE_BUTTON = Button(buttonSurface, 1410, 700, "Firerate", True, get("upgrade.json", "missileFireratePrice")[get("upgrade.json", "missileFirerateLevel")], None, buttonSurface, "Increase the firerate of the bullet")

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("font.ttf", size)

MENU_TEXT = get_font(100).render("BULLET SHOP", True, "#b68f40")
MENU_TEXT_RECT = MENU_TEXT.get_rect(center=(960, 100))
MENU_UPGRADE_1 = get_font(30).render("Bullet", True, "#b68f40")
MENU_UPGRADE_1_RECT = MENU_UPGRADE_1.get_rect(center=(640, 430))

MENU_UPGRADE_2 = get_font(30).render("Missile", True, "#b68f40")
MENU_UPGRADE_2_RECT = MENU_UPGRADE_2.get_rect(center=(1290, 430))

def shopping(projectile, stat, button, statSaveName):
    if (get("upgrade.json" ,projectile + stat + "Level") == len(get("upgrade.json" ,projectile + stat + "Upgrade"))):
        button.priceText = "Level MAX"
    else:
        post("save.json", statSaveName, get("upgrade.json", projectile + stat + "Upgrade")[get("upgrade.json", projectile + stat + "Level")])
        post("upgrade.json" ,projectile + stat + "Level",get("upgrade.json" ,projectile + stat + "Level")+1)
        button.price = get("upgrade.json", projectile + stat + "Price")[get("upgrade.json", projectile + stat + "Level")]
        return get("upgrade.json", projectile + stat + "Upgrade")[get("upgrade.json", projectile + stat + "Level")-1]

def shopBullet(SCREEN, BG, player, main_menu, gameManager, shop):
    running = True
    while running:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.blit(MENU_TEXT, MENU_TEXT_RECT)
        SCREEN.blit(MENU_UPGRADE_1, MENU_UPGRADE_1_RECT)
        SCREEN.blit(MENU_UPGRADE_2, MENU_UPGRADE_2_RECT)
        for button in [RESUME_BUTTON, SPEED_BULLET_BUTTON, DAMAGE_BULLET_BUTTON, CANONS_BULLET_BUTTON, FIRERATE_BULLET_BUTTON, SPEED_MISSILE_BUTTON, DAMAGE_MISSILE_BUTTON, CANONS_MISSILE_BUTTON, FIRERATE_MISSILE_BUTTON]:
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
                    player.bulletSpeed = shopping("bullet", "Speed", SPEED_BULLET_BUTTON, "bulletSpeed")
                    
                if DAMAGE_BULLET_BUTTON.checkForInput(MENU_MOUSE_POS, player):
                    player.bulletDamage = shopping("bullet", "Damage", DAMAGE_BULLET_BUTTON, "bulletDamage")
                    
                if CANONS_BULLET_BUTTON.checkForInput(MENU_MOUSE_POS, player):
                    player.arrayNumber = shopping("bullet", "Canons", CANONS_BULLET_BUTTON, "arrayNumber")
                    
                if FIRERATE_BULLET_BUTTON.checkForInput(MENU_MOUSE_POS, player):
                    player.timeBetweenShots = shopping("bullet", "Firerate", FIRERATE_BULLET_BUTTON, "timeBetweenShots")
                    
                if SPEED_MISSILE_BUTTON.checkForInput(MENU_MOUSE_POS, player):
                    player.missileSpeed = shopping("missile", "Speed", SPEED_MISSILE_BUTTON, "missileSpeed")
                    
                if DAMAGE_MISSILE_BUTTON.checkForInput(MENU_MOUSE_POS, player):
                    player.missileDamage = shopping("missile", "Damage", DAMAGE_MISSILE_BUTTON, "missileDamage")
                    
                if CANONS_MISSILE_BUTTON.checkForInput(MENU_MOUSE_POS, player):
                    player.missileArrayNumber = shopping("missile", "Canons", CANONS_MISSILE_BUTTON, "missileArrayNumber")
                    
                if FIRERATE_MISSILE_BUTTON.checkForInput(MENU_MOUSE_POS, player):
                    player.timeBetweenMissiles = shopping("missile", "Firerate", FIRERATE_MISSILE_BUTTON, "timeBetweenMissiles")
                    
        pygame.display.update()