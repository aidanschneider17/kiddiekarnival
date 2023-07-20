import gameLogic
import pygame
from objects import *
from timekeeping import *
import time
import random

WIDTH = 1300

WIN = pygame.display.set_mode((WIDTH, WIDTH))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0 , 255)
GREEN = (0, 255, 0)

FPS = 60

PIXEL_WIDTH = 64
PIXEL_SIZE = 10


def set_pixels():
    y = 10
    pixels = []

    for i in range(PIXEL_WIDTH):
        row = []
        x = 10
        for j in range(PIXEL_WIDTH):
            row.append(Pixel(x, y, PIXEL_SIZE, BLACK, WIN))
            x += 20
        pixels.append(row)
        y += 20

    return pixels


def draw_window(pixels):
    for i in range(len(pixels)):
        for j in range(len(pixels)):
            pixels[i][j].draw()

    pygame.display.update()


def clear_pixels(pixels):
    for i in range(len(pixels)):
        for j in range(len(pixels[i])):
            pixels[i][j].color = BLACK

    
def main():
    pixels = set_pixels()
    run = True

    title = [[]]

    clock = Clock(FPS)
    while run:
        clock.tick()
        score, run = gameLogic.play_game(pixels, clock)
        clear_pixels(pixels)

        print(score)

    pygame.quit()



if __name__ == '__main__':
    main()