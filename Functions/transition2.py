import pygame

pygame.init()
clock = pygame.time.Clock()

# Create Window
displayHeight = 1080
displayWidth = 1920
screen = pygame.display.set_mode((displayWidth, displayHeight))
pygame.display.set_caption("Transition")

def transition(surf, y, color):
    for x in range(16):
        pygame.draw.rect(surf, color, (x,16-y,1,y))
    y -= 1

running = True
transitionY = 0
subY = 0
surf = pygame.Surface((16,9))
surf.set_colorkey((0,0,0))

while running:
    screen.fill((20,20,200))
    # run the game at a constant 60fps
    clock.tick(10)
    #Close window on Escape press
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            running=False
        elif events.type == pygame.KEYDOWN:
            if events.key == pygame.K_ESCAPE:
                running=False

    if transitionY <= 32:
        transition(surf, transitionY, (255,255,255))
        new = pygame.transform.scale(surf, (displayWidth,displayHeight))
        screen.blit(new, (0,0))
        transitionY += 1
    elif transitionY > 32:
        if subY <= 32:
            transition(surf, subY, (0,0,0))
            new = pygame.transform.scale(surf, (displayWidth,displayHeight))
            screen.blit(new, (0,0))
            subY += 1
            print(subY)

    pygame.display.update()