import pygame

# from pygame.locals import *
import sys
import Ball

WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FPS = 60

pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

oBall = Ball.Ball(window, WINDOW_WIDTH, WINDOW_HEIGHT)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    oBall.update()

    window.fill("red")

    oBall.draw()

    pygame.display.update()

    clock.tick(FPS)
