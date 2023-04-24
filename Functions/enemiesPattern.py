import sys
import pygame
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
