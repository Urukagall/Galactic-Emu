import pygame
import math

class Projectile():
    def __init__(self, x, y, width, image, velocity, damage, isHoming, displayWidth, displayHeight, projectileList, player=False, enemyList = [], playerPos = (0,0)):
        self.isPlayer = player
        self.x = x
        self.y = y
        self.velocity = velocity
        self.damage = damage

        self.width = width
        self.image = image
        self.displayWidth = displayWidth
        self.displayHeight = displayHeight

        self.isHoming = isHoming
        self.enemyList = enemyList
        self.playerPos = playerPos
        self.rotationSpeed = 10

        projectileList.append(self)
        self.pos = pygame.math.Vector2(self.x, self.y)
        
        
    def update(self):
        if(self.isHoming):
           self.chase()
        else:
            self.x = self.x + self.velocity.x
            self.y = self.y + self.velocity.y

        '''The bullet is destroyed when exiting the screen'''
        if self.x < 0 - self.width:
            del(self)
        elif self.x > self.displayWidth + self.width:
            del(self)
        if self.y < 0 - self.width:
            del(self)
        elif self.y > self.displayHeight + self.width:
            del(self)

    def chase(self):
        pos = pygame.math.Vector2(self.x, self.y)
        target = pos
        if(self.isPlayer):
            min_dist = 9999
            for e in self.enemyList:
                ePos = pygame.math.Vector2(e.x, e.y)
                self.pos.distance_to(ePos)
                print(str(distance))
                if distance < min_dist:
                    print("Found closest ennemy")
                    distance = min_dist
                    target = e
            #Le missile doit trouver l'enemi le + proche
            '''radians = math.atan2(self.y - target.y, self.x - target.x)
            destX = math.cos(radians)
            destY = math.sin(radians)
            self.x += destX
            self.y += destY'''
        else:
            #le missile doit aller vers le joueur
            pass
        pass

    def rotateToTarget(self, target):
        targetPos = pygame.math.Vector2(target.x, target.y)
        
        direction = (targetPos - self.pos)
        angleTo = self.pos.angle_to(targetPos)
        self.pos.rotate(angleTo * min(self.rotationSpeed, abs(angleTo)))