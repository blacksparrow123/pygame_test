import pygame

# from pygame.locals import *
import sys
import random

WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FPS = 30
BALL_H_W = 100
MAX_WIDTH = WINDOW_WIDTH - BALL_H_W
MAX_HEIGHT = WINDOW_HEIGHT - BALL_H_W

pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()
ballImage = pygame.image.load("assets/images/ball.png")
ballX = random.randrange(MAX_WIDTH)
ballY = random.randrange(MAX_HEIGHT)
ballRect = pygame.Rect(ballX, ballY, BALL_H_W, BALL_H_W)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONUP:
            if ballRect.collidepoint(event.pos):
                ballX = random.randrange(MAX_WIDTH)
                ballY = random.randrange(MAX_HEIGHT)
                ballRect = pygame.Rect(ballX, ballY, BALL_H_W, BALL_H_W)
    window.fill("red")
    window.blit(ballImage, (ballX, ballY))
    pygame.display.update()
    clock.tick(FPS)
