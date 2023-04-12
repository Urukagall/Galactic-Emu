# Init
print("Hello Today I'm Gonna Teach You")
import pygame
import pygame.time
pygame.init()
clock = pygame.time.Clock()

# Create Window
displayHeight = 1080
displayWidth = 1920
backgroundColor = (200,200,200)
screen = pygame.display.set_mode((displayWidth, displayHeight), pygame.FULLSCREEN)


# Import Img
img_player1 = pygame.image.load("img/emeu.jpg")

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


    pressed = pygame.key.get_pressed()

    if pressed[pygame.K_z]:
        player1yVelocity = -playersSpeed

    #Draw 
    screen.fill(backgroundColor)
    pygame.display.update()
pygame.quit()