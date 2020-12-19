import pygame
import sys
import random


def flr():
    global floorx
    screen.blit(floor, (floorx, 400))
    screen.blit(floor, (floorx + 288, 400))
    if floorx <= -288:
        floorx = 0

pygame.init()
screen = pygame.display.set_mode((288, 512))
clock = pygame.time.Clock()
floor = pygame.image.load('pict/floor.png').convert()
floorx = 0

background = pygame.image.load('pict/background.png').convert()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.blit(background, (0, 0))
    flr()
    floorx -= 1
    pygame.display.update()
    clock.tick(90)
