import pygame
import sys

from Class.button import Button
from Functions.shopBullet import shopBullet
from Functions.shopConsumable import shopConsumable
from Functions.shopShip import shopShip


buttonSurface = pygame.image.load("img/ui/button.png")
buttonSurface = pygame.transform.scale(buttonSurface, (buttonSurface.get_width()/1.3, buttonSurface.get_height()/1.3))

RESUME_BUTTON = Button(buttonSurface, 960, 850, "Return", False, None, None, buttonSurface)


def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("asset/font.ttf", size)

MENU_TEXT = get_font(100).render("HOW TO PLAY", True, "#b68f40")
MENU_TEXT_RECT = MENU_TEXT.get_rect(center=(960, 100))

textHowToPlay = "Movement:\n\n\nDirectional arrows for movement\n\nSHIFT:  Slow Movement\nSPACE:  Dash\n\n\nShoot:\n\n\nW:  Main Shoot\nX:  Ultimate\n\n\nOther:\n\n\nESCAPE:  Menu\nSPACE:  Skip dialogue and intro"

# La police et la taille du texte
font = pygame.font.Font(None, 36)

# La liste des surfaces de texte pour chaque ligne
textHowToPlaySurface = []
for line in textHowToPlay.split('\n'):
    textHowToPlaySurface.append(get_font(20).render(line, True, "#b68f40"))



def howToPlay(SCREEN, BG, player, main_menu):
    running = True
    while running:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        # La position de la première ligne de texte
        x = 700
        y = 300

        # Blit chaque surface de texte sur l'écran à des positions différentes
        for text in textHowToPlaySurface:
            SCREEN.blit(text, (x, y))
            y += text.get_height()

        SCREEN.blit(MENU_TEXT, MENU_TEXT_RECT)

        for button in [RESUME_BUTTON]:
            button.changeColor(MENU_MOUSE_POS, SCREEN)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if RESUME_BUTTON.checkForInput(MENU_MOUSE_POS, player):
                    return
        pygame.display.update()
