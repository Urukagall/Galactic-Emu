import cv2
import pygame

# Initialise Pygame
pygame.init()

# Ouvre la vidéo avec OpenCV
cap = cv2.VideoCapture("video/Lake-91562.avi")

# Obtient les dimensions de la vidéo
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Initialise l'écran Pygame
screen = pygame.display.set_mode((width, height))

# Boucle principale
while True:
    # Lit une image de la vidéo avec OpenCV
    ret, frame = cap.read()
    
    # Si la lecture est terminée, sort de la boucle
    if not ret:
        break
    
    # Convertit l'image OpenCV en surface Pygame
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame = pygame.surfarray.make_surface(frame)
    
    # Affiche la surface sur l'écran Pygame
    screen.blit(frame, (0, 0))
    pygame.display.flip()
    
    # Vérifie les événements Pygame
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            cap.release()
            pygame.quit()
            quit()
            
# Libère les ressources
cap.release()
pygame.quit()
quit()
