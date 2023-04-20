import pygame
import sys

from Class.button import Button

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("font.ttf", size)

def gameOptions(SCREEN, BG, buttonSurface, player, main_menu, gameManager):
    running = True
    while running:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("OPTIONS", True, "#b68f40")
        MENU_TEXT_RECT = MENU_TEXT.get_rect(center=(960, 100))
        MENU_SOUND = get_font(30).render("Sound:%.1f" % gameManager.sound , True, "#b68f40")
        MENU_SOUND_RECT = MENU_SOUND.get_rect(center=(960, 480))

        RESUME_BUTTON = Button(buttonSurface, 960, 400, "Return", False, 0, None, buttonSurface)
        SOUNDMORE_BUTTON = Button(buttonSurface, 760, 550, "+", False, 0, None, buttonSurface)
        SOUNDLESS_BUTTON = Button(buttonSurface, 1160, 550, "-", False, 0, None, buttonSurface)
        QUIT_BUTTON = Button(buttonSurface, 960, 700, "Quit", False, 0, None, buttonSurface)

        SCREEN.blit(MENU_TEXT, MENU_TEXT_RECT)
        SCREEN.blit(MENU_SOUND, MENU_SOUND_RECT)

        for button in [RESUME_BUTTON, SOUNDMORE_BUTTON, SOUNDLESS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS, SCREEN)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if RESUME_BUTTON.checkForInput(MENU_MOUSE_POS, player):
                    main_menu()
                if SOUNDMORE_BUTTON.checkForInput(MENU_MOUSE_POS, player):
                    if gameManager.sound < 1:
                        gameManager.changeSound(gameManager.sound + 0.1)
                if SOUNDLESS_BUTTON.checkForInput(MENU_MOUSE_POS, player):
                    if gameManager.sound > 0.01:
                        gameManager.changeSound(gameManager.sound - 0.1)
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS, player):
                    running = False
                    pygame.quit()
                    sys.exit()
        pygame.display.update()