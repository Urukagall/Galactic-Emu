import pygame
import sys

from Class.button import Button
from Functions.jsonReader import *
from Functions.jsonReader import *

buttonSurface = pygame.image.load("img/assets/button.png")
buttonSurface = pygame.transform.scale(buttonSurface, (buttonSurface.get_width()/1.3, buttonSurface.get_height()/1.3))

RESUME_BUTTON = Button(buttonSurface, 960, 850, "Return", False, None, None, buttonSurface)

'''if get("save.json", "spiralAttack") == "False":
    spiralText = "Activate Spiral"
else:
    spiralText = "Deactivate Spiral"'''

# Upgrade Button Ship
LIVE_BUTTON = Button(buttonSurface, 510, 550, "Live", True, get("upgrade.json", "playerLivePrice")[get("upgrade.json", "playerLiveLevel")], None, buttonSurface, "Increase the number of live")
DASH_BUTTON = Button(buttonSurface, 760, 550, "Dash Cooldown", True, get("upgrade.json", "playerDashPrice")[get("upgrade.json", "playerDashLevel")], None, buttonSurface, "Increase the dash cooldown timer")
SHIELD_BUTTON = Button(buttonSurface, 510, 700, "Shield", True, get("upgrade.json", "playerLivePrice")[get("upgrade.json", "playerLiveLevel")], None, buttonSurface, "Increase invulnerability time")
SPEED_BUTTON = Button(buttonSurface, 760, 700, "Speed", True, get("upgrade.json", "playerSpeedPrice")[get("upgrade.json", "playerSpeedLevel")], None, buttonSurface, "Increase the speed of the ship")

# Upgrade Button bullet
SPEED_BULLET_BUTTON = Button(buttonSurface, 1160, 550, "Speed", False, None, None, buttonSurface, "Increase the number of live")
DAMAGE_BUTTON = Button(buttonSurface, 1410, 550, "Damage", False, None, None, buttonSurface, "Increase the dash cooldown timer")
CANONS_BUTTON = Button(buttonSurface, 1160, 700, "Canons", False, None, None, buttonSurface, "Acquire the spiral attack")
FIRERATE_BUTTON = Button(buttonSurface, 1410, 700, "Firerate", False, None, None, buttonSurface, "Increase the speed when normal movement and decrease it when slow movement")

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("font.ttf", size)

MENU_TEXT = get_font(100).render("SHIP SHOP", True, "#b68f40")
MENU_TEXT_RECT = MENU_TEXT.get_rect(center=(960, 100))
MENU_UPGRADE = get_font(30).render("Upgrade", True, "#b68f40")
MENU_UPGRADE_RECT = MENU_UPGRADE.get_rect(center=(960, 480))


def shopping(stat, button, statSaveName):
    if (get("upgrade.json" ,"player" + stat + "Level") == len(get("upgrade.json" ,"player" + stat + "Upgrade"))):
        button.priceText = "Level MAX"
    else:
        post("save.json", statSaveName, get("upgrade.json", "player" + stat + "Upgrade")[get("upgrade.json", "player" + stat + "Level")])
        post("upgrade.json" ,"player" + stat + "Level",get("upgrade.json" ,"player" + stat + "Level")+1)
        button.price = get("upgrade.json", "player" + stat + "Price")[get("upgrade.json", "player" + stat + "Level")]
        return get("upgrade.json", "player" + stat + "Upgrade")[get("upgrade.json", "player" + stat + "Level")-1]

def shopShip(SCREEN, BG, player, main_menu, gameManager, shop):
    running = True
    while running:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.blit(MENU_TEXT, MENU_TEXT_RECT)
        # SCREEN.blit(MENU_UPGRADE, MENU_UPGRADE_RECT)

        for button in [RESUME_BUTTON, LIVE_BUTTON, DASH_BUTTON, SHIELD_BUTTON, SPEED_BUTTON, SPEED_BULLET_BUTTON, DAMAGE_BUTTON, CANONS_BUTTON, FIRERATE_BUTTON]:
            button.changeColor(MENU_MOUSE_POS, SCREEN)
            button.update(SCREEN)
            
                    
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if RESUME_BUTTON.checkForInput(MENU_MOUSE_POS, player):
                    shop(SCREEN, BG, player, main_menu, gameManager)
                    
                if LIVE_BUTTON.checkForInput(MENU_MOUSE_POS, player):
                    player.lives = shopping("Live", LIVE_BUTTON, "money")
                    
                if SPEED_BUTTON.checkForInput(MENU_MOUSE_POS, player):
                    player.basicSpeed = shopping("Speed", SPEED_BUTTON, "speed")
                    
                if DASH_BUTTON.checkForInput(MENU_MOUSE_POS, player):
                    player.cooldownDash = shopping("Dash", DASH_BUTTON, "cooldownDash")
                    
        pygame.display.update()