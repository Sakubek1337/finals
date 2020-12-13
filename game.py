import pygame
import sys

pygame.init()
window = pygame.display.set_mode((500, 600))
pygame.display.set_caption('Blappy Fird')
clock = pygame.time.Clock()

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    window.fill((176, 200, 50))
    pygame.draw.rect(window, (0, 255, 255), (0, 0, 50, 200))
    pygame.display.update()
    clock.tick(120)
