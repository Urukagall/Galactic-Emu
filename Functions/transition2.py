import pygame

pygame.init()
clock = pygame.time.Clock()

# Create Window
displayHeight = 1080
displayWidth = 1920
screen = pygame.display.set_mode((displayWidth, displayHeight))
pygame.display.set_caption("Transition")

def transition(screen, y, color):
    surf = pygame.Surface((16, 9))
    for x in range(16):
        y -= 1
        pygame.draw.rect(surf, color, (x,16-y,1,y))
    return surf

running = True
transitionY = 0
while running:
    # run the game at a constant 60fps
    clock.tick(60)
    #Close window on Escape press
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            running=False
        elif events.type == pygame.KEYDOWN:
            if events.key == pygame.K_ESCAPE:
                running=False
    
    if transitionY <= 32:
        surf = transition(screen, transitionY, (255,255,255))
        surf = pygame.transform.scale(surf, (displayWidth,displayHeight))
        screen.blit(surf, (0,0))
        transitionY += 1
    elif transitionY > 32:
        #invert
        pass
    
    pygame.display.update()

pygame.quit()