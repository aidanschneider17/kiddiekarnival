import gameLogic
from objects import *
from timekeeping import *
import time
import random

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0 , 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
ORANGE = (255, 136, 0)

FPS = 60

PIXEL_WIDTH = 64
PIXEL_SIZE = 10

SPLASH_TEXT = [[1, 0, 1, 0, 1, 1, 1, 0],
               [1, 0, 1, 0, 0, 1, 0, 0],
               [1, 0, 1, 0, 0, 1, 0, 0],
               [1, 1, 1, 0, 0, 1, 0, 0],
               [1, 0, 1, 0, 0, 1, 0, 0],
               [1, 0, 1, 0, 0, 1, 0, 0],
               [1, 0, 1, 0, 0, 1, 0, 0],
               [1, 0, 1, 0, 1, 1, 1, 0]]

def show_score(score, matrix):
    score_text = Number(len(matrix.pixels)//2, len(matrix.pixels)//2, ORANGE, matrix.pixels, num=score)
    score_text.draw()
    matrix.update()
    time.sleep(5)

def clear_pixels(pixels):
    for i in range(len(pixels)):
        for j in range(len(pixels[i])):
            pixels[i][j] = BLACK

    
def main():
    matrix = Matrix_Update()
    splash = Number(len(matrix.pixels)//2, len(matrix.pixels)//2, YELLOW, matrix.pixels, num_shape=SPLASH_TEXT)
    
    run = True

    title = [[]]

    clock = Clock(FPS)
    splash_time = Timer(FPS, 2)
    while run:
        clock.tick()
        splash_time.tick()

        splash.draw()

        if splash_time.completed:
            clear_pixels(matrix.pixels)
            score, run = gameLogic.play_game(matrix, clock)
            clear_pixels(matrix.pixels)
            show_score(score, matrix)
            clear_pixels(matrix.pixels)

            splash_time.reset()

        matrix.update()



if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt as e:
        print("Done")