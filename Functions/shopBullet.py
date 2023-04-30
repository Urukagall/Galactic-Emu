import pygame
import sys

from Class.button import Button
from Functions.jsonReader import *


buttonSurface = pygame.image.load("img/ui/button.png")
buttonSurface = pygame.transform.scale(buttonSurface, (buttonSurface.get_width()/1.3, buttonSurface.get_height()/1.3))
bulletNumberUp = pygame.image.load("img/ui/bulletCanons.png")
bulletNumberUp = pygame.transform.scale(bulletNumberUp, (200, 75))
bulletSpeedUp = pygame.image.load("img/ui/bulletSpeed.png")
bulletSpeedUp = pygame.transform.scale(bulletSpeedUp, (200, 75))
bulletFirerateUp = pygame.image.load("img/ui/bulletFireRate.png")
bulletFirerateUp = pygame.transform.scale(bulletFirerateUp, (200, 75))
bulletDamage = pygame.image.load("img/ui/bulletDamage.png")
bulletDamage = pygame.transform.scale(bulletDamage, (200, 75))
missileNumberUp = pygame.image.load("img/ui/missileCanons.png")
missileNumberUp = pygame.transform.scale(missileNumberUp, (200, 75))
missileSpeedUp = pygame.image.load("img/ui/missileSpeed.png")
missileSpeedUp = pygame.transform.scale(missileSpeedUp, (200, 75))
missileFirerateUp = pygame.image.load("img/ui/missileFireRate.png")
missileFirerateUp = pygame.transform.scale(missileFirerateUp, (200, 75))
missileDamage = pygame.image.load("img/ui/missileDamage.png")
missileDamage = pygame.transform.scale(missileDamage, (200, 75))
imgCoin = pygame.image.load("img/ui/coin.png")
imgCoin = pygame.transform.scale(imgCoin, (80, 40))

RESUME_BUTTON = Button(buttonSurface, 960, 850, "Return", False, None, None, buttonSurface)

# Upgrade Button Bullet 1
SPEED_BULLET_BUTTON = Button(bulletSpeedUp, 550, 550, "", True, get("upgrade.json", "bulletSpeedPrice")[get("upgrade.json", "bulletSpeedLevel")], None, buttonSurface, "Increase the speed of the bullet")
DAMAGE_BULLET_BUTTON = Button(bulletDamage, 800, 550, "", True, get("upgrade.json", "bulletDamagePrice")[get("upgrade.json", "bulletDamageLevel")], None, buttonSurface, "Increase the damage of the bullet")
CANONS_BULLET_BUTTON = Button(bulletNumberUp, 550, 700, "", True, get("upgrade.json", "bulletCanonsPrice")[get("upgrade.json", "bulletCanonsLevel")], None, buttonSurface, "Shoot more bullet")
FIRERATE_BULLET_BUTTON = Button(bulletFirerateUp, 800, 700, "", True, get("upgrade.json", "bulletFireratePrice")[get("upgrade.json", "bulletFirerateLevel")], None, buttonSurface, "Increase the firerate of the bullet")

# Upgrade Button bullet 2
SPEED_MISSILE_BUTTON = Button(missileSpeedUp, 1150, 550, "", True, get("upgrade.json", "missileSpeedPrice")[get("upgrade.json", "missileSpeedLevel")], None, buttonSurface, "Increase the speed of the bullet")
DAMAGE_MISSILE_BUTTON = Button(missileDamage, 1400, 550, "", True, get("upgrade.json", "missileDamagePrice")[get("upgrade.json", "missileDamageLevel")], None, buttonSurface, "Increase the damage of the bullet")
CANONS_MISSILE_BUTTON = Button(missileNumberUp, 1150, 700, "", True, get("upgrade.json", "missileCanonsPrice")[get("upgrade.json", "missileCanonsLevel")], None, buttonSurface, "Shoot more bullet")
FIRERATE_MISSILE_BUTTON = Button(missileFirerateUp, 1400, 700, "", True, get("upgrade.json", "missileFireratePrice")[get("upgrade.json", "missileFirerateLevel")], None, buttonSurface, "Increase the firerate of the bullet")

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("asset/font.ttf", size)

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
        MENU_MONEY = get_font(20).render(str(player.money), True, "#b68f40")
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.blit(MENU_TEXT, MENU_TEXT_RECT)
        SCREEN.blit(MENU_UPGRADE_1, MENU_UPGRADE_1_RECT)
        SCREEN.blit(MENU_UPGRADE_2, MENU_UPGRADE_2_RECT)
        
        SCREEN.blit(imgCoin,(0 ,50))
        SCREEN.blit(MENU_MONEY, (100,60))
        
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
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    shop(SCREEN, BG, player, main_menu, gameManager)
        pygame.display.update()