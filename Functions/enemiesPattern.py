import sys
import pygame
import math
sys.path.append("/Mini-studio/Class")
#from Class.enemy import Enemy

def firstPattern(Enemy):
    
    if Enemy.x <= 0:
        Enemy.facing = "right"
        Enemy.patternStep = 0
    elif Enemy.x >= 1920 - Enemy.size:
        Enemy.facing = "left"
        Enemy.patternStep = 0

    if Enemy.facing == "right" and Enemy.x == 0:
        Enemy.move(Enemy.speed, Enemy.speed/2)
    elif Enemy.facing == "right" and Enemy.x%6 == 0 and Enemy.x < 1920//2:
        Enemy.move(Enemy.speed, 0)
    elif Enemy.facing == "right" and Enemy.x<= 1920//2:
        Enemy.move(Enemy.speed, Enemy.speed/2)
    
    if Enemy.facing == "right" and Enemy.x > 1920//2 and Enemy.x%6  == 0:
        Enemy.move(Enemy.speed, 0)
    elif Enemy.facing == "right" and Enemy.x > 1920//2:
        Enemy.move(Enemy.speed, -Enemy.speed/2)

    if Enemy.facing == "left" and Enemy.x == 1920//2:
        Enemy.move(-Enemy.speed, Enemy.speed/2)
    elif Enemy.facing == "left" and (Enemy.x)%6 == 0 and Enemy.x < 1920//2:
        Enemy.move(-Enemy.speed, 0)
    elif Enemy.facing == "left" and Enemy.x <= 1920//2: 
        Enemy.move(-Enemy.speed, Enemy.speed/2)
    
    if Enemy.facing == "left" and Enemy.x > 1920//2 and Enemy.x%6  == 0:
        Enemy.move(-Enemy.speed, 0)
    elif Enemy.facing == "left" and Enemy.x > 1920//2:
        Enemy.move(-Enemy.speed, -Enemy.speed/2)

    Enemy.patternStep += 1
    Enemy.bulletHandler.move(Enemy.x, Enemy.y)

def miniBossPatern(Enemy):
    if Enemy.health > 500:
        if Enemy.x <= 0:
            Enemy.facing = "right"
        elif Enemy.x >= 1920 - Enemy.size:
            Enemy.facing = "left"

        if Enemy.facing == "left":
            Enemy.move(-1,0)
        elif Enemy.facing == "right":
            Enemy.move(1, 0)
    
    if Enemy.health <= 500:
        if Enemy.x == 640 and Enemy.y == 0:
            Enemy.facing = "right"
        if Enemy.x == 1280 and Enemy.y == 0:
            Enemy.facing = "down"
        if Enemy.x == 1280 and Enemy.y == 360:
            Enemy.facing = "left"
        if Enemy.x == 640 and Enemy.y == 360:
            Enemy.facing = "up"

        if Enemy.facing == "right":
            Enemy.move(1, 0)
        elif Enemy.facing == "down":
            Enemy.move(0, 1)
        elif Enemy.facing == "left":
            Enemy.move(-1, 0)
        elif Enemy.facing == "up":
            Enemy.move(0, -1)

def bossPattern(Enemy, patternNum):
    if patternNum == 1:
        if Enemy.x <= 0:
            Enemy.facing = "right"
        elif Enemy.x >= 1920 - Enemy.size:
            Enemy.facing = "left"

        if Enemy.facing == "left":
            Enemy.move(-1,0)
        elif Enemy.facing == "right":
            Enemy.move(1, 0)
