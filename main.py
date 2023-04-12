# Init
# print("Hello Today I'm Gonna Teach You")
# import pygame
# import pygame.time
# pygame.init()
# clock = pygame.time.Clock()

# # Create Window
# displayHeight = 1080
# displayWidth = 1920
# backgroundColor = (200,200,200)
# screen = pygame.display.set_mode((displayWidth, displayHeight), pygame.FULLSCREEN)


# # Main Loop
# running = True
# while (running):
#     # run the game at a constant 60fps
#     clock.tick(60)
#     #Did the user clicked the close button ?
#     for events in pygame.event.get():
#         if events.type == pygame.QUIT:
#             running=False
#         elif events.type == pygame.KEYDOWN:
#             if events.key == pygame.K_ESCAPE:
#                 running=False

#     #Draw 
#     screen.fill(backgroundColor)
#     pygame.display.update()
# pygame.quit()

import pygame 
import math

pygame.init()

clock = pygame.time.Clock()
FPS = 60 

SCREEN_WIDTH = 1500 
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Endless Scroll")

bg = pygame.image.load("img/emeu.jpg").convert()
bg_width = bg.get_width()
bg_rect = bg.get_rect()

scroll = 0 
tiles = math.ceil(SCREEN_WIDTH / bg_width) + 1


run = True 
while run:

    clock.tick(FPS)

    #draw scrolling background 
    for i in range(0, tiles):
      screen.blit(bg,(i * bg_width + scroll, 0))
      bg_rect.x = i * bg_width + scroll
      pygame.draw.rect(screen, (255, 0, 0), bg_rect, 1)

    #scroll background
    scroll -= 5

    #reset scroll
    if abs (scroll) > bg_width:
        scroll = 0

    #envent handler 
    for event in pygame.event.get(): 
      if event.type == pygame.QUIT: 
            run = False 

pygame.display.update()

pygame.quit()