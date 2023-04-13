import pygame

class Projectile():

    def __init__(self, x, y, width, image):
        self.x = x
        self.y = y
        self.width = width
        self.image = image
        self.velocity = 4
