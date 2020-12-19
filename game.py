import pygame
import sys
import random


def flr():
    global floorx
    screen.blit(floor, (floorx, 456))
    screen.blit(floor, (floorx + 288, 456))
    if floorx <= -288:
        floorx = 0


def create_pipe():
    y = random.choice(heights)
    bot_pipe = pipe.get_rect(midtop=(304, y))
    top_pipe = pipe.get_rect(midbottom=(304, y - 150))
    return bot_pipe, top_pipe


def move_pipes(pipez):
    for pipee in pipez:
        pipee.centerx -= 2.125
    return pipez


def draw_pipes(pipez):
    for pipee in pipez:
        if pipee.bottom >= 500:
            screen.blit(pipe, pipee)
        else:
            flip = pygame.transform.flip(pipe, False, True)
            screen.blit(flip, pipee)


pygame.init()
screen = pygame.display.set_mode((288, 512))
clock = pygame.time.Clock()
floor = pygame.image.load('pict/floor.png').convert()
floorx = 0

background = pygame.image.load('pict/background.png').convert()
bird = pygame.image.load('pict/bird-midflap.png').convert()
bird_rect = bird.get_rect(center=(50, 256))
grav = 0.25
bird_mv = 0

pipe = pygame.image.load('pict/pipe.png').convert()
pipes = []
heights = [200, 250, 300, 350, 400]
spawnpipes = pygame.USEREVENT
pygame.time.set_timer(spawnpipes, 1450)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_mv = 0
                bird_mv -= 7.5
        if event.type == spawnpipes:
            pipes.extend(create_pipe())

    screen.blit(background, (0, 0))

    screen.blit(bird, bird_rect)
    bird_mv += grav
    bird_rect.centery += bird_mv

    pipes = move_pipes(pipes)
    draw_pipes(pipes)

    flr()
    floorx -= 3
    pygame.display.update()
    clock.tick(90)
