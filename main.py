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
TARGET_X = 400
TARGET_Y = 320
TARGET_WIDTH_HEIGHT = 120
N_PIXELS_TO_MOVE = 3

pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()
ballImage = pygame.image.load("assets/images/ball.png")
targetImage = pygame.image.load('assets/images/target.jpg')
ballX = random.randrange(MAX_WIDTH)
ballY = random.randrange(MAX_HEIGHT)
targetRect = pygame.Rect(TARGET_X, TARGET_Y, TARGET_WIDTH_HEIGHT, TARGET_WIDTH_HEIGHT)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keyPressedTuple = pygame.key.get_pressed()
    if keyPressedTuple[pygame.K_LEFT]:
        ballX = ballX - N_PIXELS_TO_MOVE
    if keyPressedTuple[pygame.K_RIGHT]:
        ballX = ballX + N_PIXELS_TO_MOVE
    if keyPressedTuple[pygame.K_UP]:
        ballY = ballY - N_PIXELS_TO_MOVE
    if keyPressedTuple[pygame.K_DOWN]:
        ballY = ballY + N_PIXELS_TO_MOVE
    print(keyPressedTuple)
    ballRect = pygame.Rect(ballX, ballY, BALL_H_W, BALL_H_W)
    if ballRect.colliderect(targetRect):
        print('Ball is touching the target')
    window.fill("red")
    window.blit(ballImage, (ballX, ballY))
    window.blit(targetImage, (TARGET_X, TARGET_Y))
    pygame.display.update()
    clock.tick(FPS)
