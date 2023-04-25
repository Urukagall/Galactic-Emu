import cv2

# Lecture de la vidéo
cap = cv2.VideoCapture('video/Lake-91562.avi')

# Boucle jusqu'à la fin de la vidéo
while cap.isOpened():
    # Capture des images
    ret, frame = cap.read()
    
    # Si la capture a réussi
    if ret:
        # Retourner la vidéo
        frame = cv2.flip(frame, 180)

        # Affichage de la vidéo
        cv2.imshow('Video', frame)

        # Attendre 25 millisecondes avant d'afficher l'image suivante
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        break

# Libération des ressources
cap.release()
cv2.destroyAllWindows()
