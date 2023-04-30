#Imporwwwt librairies
import pygame, sys
import pygame.time

#Import Classes
from Class.player import Player
from Class.button import Button
from Class.gameManager import GameManager
from Functions.jsonReader import *

#Import Patterns
from Functions.enemiesPattern import *
from Functions.options import gameOptions
from Functions.shop import shop
from Functions.play import *
from Functions.credits import credits
from Functions.howToPlay import howToPlay
from Functions.saveReader import saveReader
from Functions.darken import darken
from SaveFiles.templatePaste import templatePaste

pygame.init()  

# Logo windows
icon = pygame.image.load("img/emeu.jpg") 
pygame.display.set_icon(icon)

buttonSurface = pygame.image.load("img/ui/button.png")
buttonSurface = pygame.transform.scale(buttonSurface, (buttonSurface.get_width()/1.3, buttonSurface.get_height()/1.3))

logo = pygame.image.load("img/ui/logo.png")
logo = pygame.transform.scale(logo, (logo.get_width()/1.3, logo.get_height()/1.3))

#Import missile model
missile = pygame.image.load("img/bullets/missile.png")
missile = pygame.transform.scale(missile, (missile.get_width(), missile.get_height()))
missileWidth = missile.get_width()

#Import bullets 
classicBullet =  pygame.image.load("img/bullets/bullet.png")
classicBullet = pygame.transform.scale(classicBullet, (classicBullet.get_width()*2, classicBullet.get_height()*2))

# Import Carreau modele
carreauBlue =  pygame.image.load("img/bullets/carreau.png")
carreauBlue = pygame.transform.scale(carreauBlue, (carreauBlue.get_width()*2, carreauBlue.get_height()*2))


#projectileList & CD
projectileList = []

imgPlayer = pygame.image.load("img/ships/player.png")
imgPlayer = pygame.transform.scale(imgPlayer, (50, 50))

imgEmeu = pygame.image.load("img/avatar/heros-comesback.png")
# imgEmeu = pygame.transform.scale(imgEmeu, (50, 50))
imgColonel = pygame.image.load("img/avatar/colonel.png")
# imgColonel = pygame.transform.scale(imgColonel, (50, 50))

SCREEN = pygame.display.set_mode((1920, 1080))
pygame.display.set_caption("Menu")  

BG = pygame.image.load("img/bgs/background.png")
BG = pygame.transform.scale(BG, (1920, 1080))

gameManager = GameManager()

menuMusic = pygame.mixer.Sound("sound/menu_music.ogg")
menuMusic.set_volume(0.2 * gameManager.sound)

darkCarreau = darken(carreauBlue,45).convert_alpha()
darkBullet = darken(classicBullet).convert_alpha()
darkMissile = darken(missile,60).convert_alpha()

imgPlayer = pygame.image.load("img/ships/player.png").convert_alpha()
imgPlayer = pygame.transform.scale(imgPlayer, (50, 50))
imgPlayerShield = pygame.image.load("img/ships/playerShield.png").convert_alpha()
imgPlayerShield = pygame.transform.scale(imgPlayerShield, (50, 50))

player = Player(10, 5, 50, 1920, 1080, 30, 120, 15, 5, projectileList, darkBullet, darkMissile, darkCarreau, imgPlayer, imgPlayerShield)

textEpilepsy = "Warning\n\nThis game contains lots of projectiles and colors\nwhich results in flashing lights.\n\nIt might trigger seizure for people with\n photosensitive epilepsy."
textEpilepsySurface = []
textEpilepsyRect = []
for line in textEpilepsy.split('\n'):
    textEpilepsySurface.append(get_font(20).render(line, True, "#b68f40"))

# Take the save from the save.json
saveReader(player)

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("asset/font.ttf", size)

def main_menu(alert=True):
    isPaused = True
    if alert:
        if isPaused:

            pausedRect = pygame.Surface((1920,1080)) 
            pausedRect.set_alpha(128)
            pausedRect.fill((0,0,0))           
            SCREEN.blit(pausedRect, (0,0))
            # La position de la première ligne de texte
            x = 960
            y = 300

            # Blit chaque surface de texte sur l'écran à des positions différentes

            for text in textEpilepsySurface:

                SCREEN.blit(text, text.get_rect(center=(x, y)))
                y += text.get_height()

            epilepsyWarningText = get_font(90).render("EPILEPSY WARNING !!!", True, "#b68f40")
            epilepsyRect = epilepsyWarningText.get_rect(center=(960, 100))
            SCREEN.blit(epilepsyWarningText,epilepsyRect)
            spaceText = get_font(20).render("press any key", True, "#b68f40")
            spaceRect = spaceText.get_rect(center=(960, 950))
            SCREEN.blit(spaceText,spaceRect)

            while True:
                event = pygame.event.poll()

                if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                    isPaused = False
                    break

                pygame.display.flip()
    running = True
    while running:
        if menuMusic.get_num_channels() == 0:
            menuMusic.play(-1)  
        SCREEN.blit(BG, (0, 0))
        SCREEN.blit(imgEmeu, (-100,300))
        SCREEN.blit(imgColonel, (1000,300))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(960, 100))

        PLAY_BUTTON = Button(buttonSurface, 960, 250, "Play", False, None, play, buttonSurface)
        SHOP_BUTTON = Button(buttonSurface, 960, 400, "Shop", False, None, gameOptions, buttonSurface)
        OPTIONS_BUTTON = Button(buttonSurface, 960, 550, "Options", False, None, gameOptions, buttonSurface)
        HOW_TO_PLAY_BUTTON = Button(buttonSurface, 960, 700, "How to play", False, None, howToPlay, buttonSurface)
        CREDITS_BUTTON = Button(buttonSurface, 960, 850, "Credit", False, None, credits, buttonSurface)
        QUIT_BUTTON = Button(buttonSurface, 960, 1000, "Quit", False, None, None, buttonSurface)

        SCREEN.blit(logo, (960 - (logo.get_width() / 2),0))

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, SHOP_BUTTON, QUIT_BUTTON, HOW_TO_PLAY_BUTTON, CREDITS_BUTTON]:
            button.changeColor(MENU_MOUSE_POS, SCREEN)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS, player):
                    menuMusic.stop()
                    play(player, gameManager)
                if SHOP_BUTTON.checkForInput(MENU_MOUSE_POS, player):
                    shop(SCREEN, BG, player, main_menu, gameManager)
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS, player):
                    gameOptions(SCREEN, BG, player, main_menu, gameManager, menuMusic)
                if HOW_TO_PLAY_BUTTON.checkForInput(MENU_MOUSE_POS, player):
                    howToPlay(SCREEN, BG, player, main_menu)
                if CREDITS_BUTTON.checkForInput(MENU_MOUSE_POS, player):
                    credits(SCREEN, BG, player, main_menu)
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS, player):
                    running = False
                    pygame.quit()
                    sys.exit()
        pygame.display.update()
main_menu()
