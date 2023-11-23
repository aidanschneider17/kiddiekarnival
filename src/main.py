import gameLogic
from objects import *
from timekeeping import *
import time
import random
import tty, sys, termios
import threading

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

keys_pressed = dict(('w', False))

def show_score(score, matrix):
    score_text = Number(len(matrix.pixels)//2, len(matrix.pixels)//2, ORANGE, matrix.pixels, num=score)
    score_text.draw()
    matrix.update()
    time.sleep(5)

def clear_pixels(pixels):
    for i in range(len(pixels)):
        for j in range(len(pixels[i])):
            pixels[i][j] = BLACK

def get_input():
    global keys_pressed
    found = True

    while found:
    key = sys.stdin.buffer.read(1)[0]
        if key == 119:
            keys_pressed['w'] = True
            found = False
    
def main():
    try:
        matrix = Matrix_Update()
        splash = Custom_Shape(0, 0, matrix.pixels, 'splash.csv')
        filedescriptors = termios.tcgetattr(sys.stdin)
        tty.setcbreak(sys.stdin)
        
        run = True

        title = [[]]

        clock = Clock(FPS)

        t = threading.Thread(target=get_input, daemon=True)
        t.start()
        while run:
            clock.tick()

            splash.draw()

            if keys_pressed['w']:
                clear_pixels(matrix.pixels)
                score, run = gameLogic.play_game(matrix, clock)
                clear_pixels(matrix.pixels)
                show_score(score, matrix)
                clear_pixels(matrix.pixels)
                t.start()

            matrix.update()
    except KeyboardInterrupt as e:
        print("Done")
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, filedescriptors)



if __name__ == '__main__':
    main()