import time
import pygame
from gui import *
from game import *

pygame.init()

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
display = pygame.display
clock = pygame.time.Clock()
done = False

# White background
background_color = (255, 255, 255)

game = Game()

counter = 0


start = time.time()
while not done:
    counter += 1

    clock.tick(60)

    screen.fill(background_color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    if counter >= 5:
        game.tick()

    if counter >= 205:
        break

    game.render(screen)
    display.flip()
