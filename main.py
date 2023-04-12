# Init
import pygame
import pygame.time
from sys import exit
pygame.init()
clock = pygame.time.Clock()

# Create Window
displayHeight = 720
displayWidth = 1080
backgroundColor = (200,200,200)
screen = pygame.display.set_mode((displayWidth, displayHeight), pygame.RESIZABLE)
pygame.display.set_caption("Emeu war")

test_surface = pygame.Surface((100,200))

# Main Loop
running = True
while (running):
    # run the game at a constant 60fps
    clock.tick(60)
    #Did the user clicked the close button ?
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            running=False
        elif events.type == pygame.KEYDOWN:
            if events.key == pygame.K_ESCAPE:
                running=False

    #Draw 
    screen.fill(backgroundColor)
    pygame.display.update()
pygame.quit()