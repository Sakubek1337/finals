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


def check_coll(pipez):
    for pipee in pipez:
        if bird_rect.colliderect(pipee):
            return False

    if bird_rect.top <= -50 or bird_rect.bottom >= 456:
        return False

    return True


def rotate(birb):
    new_bird = pygame.transform.rotozoom(birb, -bird_mv * 3, 1).convert_alpha()
    return new_bird


def bird_animation():
    new_bird = bird_frames[bird_index]
    new_bird_rect = new_bird.get_rect(center=(50, bird_rect.centery))
    return new_bird, new_bird_rect


pygame.init()
is_going = True
screen = pygame.display.set_mode((288, 512))
clock = pygame.time.Clock()
floor = pygame.image.load('pict/floor.png').convert()
floorx = 0

background = pygame.image.load('pict/background.png').convert()
bird_down = pygame.image.load('pict/bird-downflap.png').convert_alpha()
bird_mid = pygame.image.load('pict/bird-midflap.png').convert_alpha()
bird_up = pygame.image.load('pict/bird-upflap.png').convert_alpha()
bird_frames = [bird_down, bird_mid, bird_up]
bird_index = 0
bird = bird_frames[bird_index]

birdflap = pygame.USEREVENT + 1
pygame.time.set_timer(birdflap, 200)

bird_rect = bird.get_rect(center=(50, 256))
grav = 0.25
bird_mv = 0

pipe = pygame.image.load('pict/pipe.png').convert()
pipes = []
heights = [200, 300, 400]
spawnpipes = pygame.USEREVENT
pygame.time.set_timer(spawnpipes, 1450)
score = 0
highscore = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and is_going:
                bird_mv = 0
                bird_mv -= 7.5
            if event.key == pygame.K_SPACE and not is_going:
                is_going = True
                pipes.clear()
                bird_mv = 0
                bird_rect.centery = 100

        if event.type == spawnpipes:
            pipes.extend(create_pipe())

        if event.type == birdflap:
            if bird_index < 2:
                bird_index += 1
            else:
                bird_index = 0

            bird, bird_rect = bird_animation()

    screen.blit(background, (0, 0))
    if is_going:
        is_going = check_coll(pipes)
        rotated_bird = rotate(bird)
        screen.blit(rotated_bird, bird_rect)
        bird_mv += grav
        bird_rect.centery += bird_mv

        pipes = move_pipes(pipes)
        draw_pipes(pipes)

    flr()
    floorx -= 3
    pygame.display.update()
    clock.tick(90)
