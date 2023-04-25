from Functions.jsonReader import *
import pygame

def saveReader (player):
    player.money = get("save.json", "money")
    player.speed = get("save.json", "speed")
    player.lives = get("save.json", "lives")
    player.cooldownDash = get("save.json", "cooldownDash")
    player.dashInvulnerability = get("save.json", "dashInvulnerability")
    player.bulletSpeed = get("save.json", "bulletSpeed")
    player.arrayNumber = get("save.json", "arrayNumber")
    player.bulletDamage = get("save.json", "bulletDamage")
    player.timeBetweenShots = get("save.json", "timeBetweenShots")
    player.missileSpeed = get("save.json", "missileSpeed")
    player.missileArrayNumber = get("save.json", "missileArrayNumber")
    player.missileDamage = get("save.json", "missileDamage")
    player.timeBetweenMissiles = get("save.json", "timeBetweenMissiles")
    imgPlayer = pygame.image.load("img/ships/" + get("save.json", "skin"))
    imgPlayer = pygame.transform.scale(imgPlayer, (50, 50))
    player.img = imgPlayer
    imgPlayerShield = pygame.image.load("img/ships/" + get("save.json", "skinShield"))
    imgPlayerShield = pygame.transform.scale(imgPlayerShield, (50, 50))
    player.imgShield = imgPlayerShield