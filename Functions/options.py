import pygame
import sys

from Class.button import Button

buttonAmeliorationSurface = pygame.image.load("img/ui/buttonAmelioration.png")
buttonAmeliorationSurface = pygame.transform.scale(buttonAmeliorationSurface, (buttonAmeliorationSurface.get_size()[0] * 2, buttonAmeliorationSurface.get_size()[1] * 2))

buttonSurface = pygame.image.load("img/ui/button.png")
buttonSurface = pygame.transform.scale(buttonSurface, (buttonSurface.get_width()/1.3, buttonSurface.get_height()/1.3))

RESUME_BUTTON = Button(buttonSurface, 960, 700, "Return", False, None, None, buttonSurface)
SOUNDMORE_BUTTON = Button(buttonAmeliorationSurface, 760, 550, "+", False, None, None, buttonSurface)
SOUNDLESS_BUTTON = Button(buttonAmeliorationSurface, 1160, 550, "-", False, None, None, buttonSurface)

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("asset/font.ttf", size)



def gameOptions(SCREEN, BG, player, main_menu, gameManager, menuMusic):
    running = True
    while running:
        SCREEN.blit(BG, (0, 0))
        MENU_MOUSE_POS = pygame.mouse.get_pos()
        MENU_TEXT = get_font(100).render("OPTIONS", True, "#b68f40")
        MENU_TEXT_RECT = MENU_TEXT.get_rect(center=(960, 100))
        MENU_SOUND = get_font(30).render("Sound:%.1f" % gameManager.sound , True, "#b68f40")
        MENU_SOUND_RECT = MENU_SOUND.get_rect(center=(960, 480))

        SCREEN.blit(MENU_TEXT, MENU_TEXT_RECT)
        SCREEN.blit(MENU_SOUND, MENU_SOUND_RECT)

        for button in [RESUME_BUTTON, SOUNDMORE_BUTTON, SOUNDLESS_BUTTON]:
            button.changeColor(MENU_MOUSE_POS, SCREEN)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if RESUME_BUTTON.checkForInput(MENU_MOUSE_POS, player):
                    return
                if SOUNDMORE_BUTTON.checkForInput(MENU_MOUSE_POS, player):
                    if gameManager.sound < 1:
                        gameManager.changeSound(gameManager.sound + 0.1)
                        menuMusic.set_volume(0.2 * gameManager.sound)
                if SOUNDLESS_BUTTON.checkForInput(MENU_MOUSE_POS, player):
                    if gameManager.sound > 0.01:
                        gameManager.changeSound(gameManager.sound - 0.1)
                        menuMusic.set_volume(0.2 * gameManager.sound)
        pygame.display.update()
