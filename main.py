import pygame
#from pygame.locals import *
import sys

WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FPS = 30
BALL_H_W = 100

pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    window.fill('red')
    pygame.display.update()
    clock.tick(FPS)