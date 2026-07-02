import gameLogic
from objects import *
from timekeeping import *
import time
import random
import tty, sys, termios
import threading

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (255, 0, 255)

FPS = 60

PIXEL_WIDTH = 64
PIXEL_SIZE = 10

key_pressed = dict([('d', False)])
listen = True

def show_score(score, matrix):
    splash = Custom_Shape(8, 10, matrix.pixels, 'WallBall/scoreSign.csv')
    score_text = Number(len(matrix.pixels)//2, len(matrix.pixels)//2, PURPLE, matrix.pixels, num=score)
    score_text.draw()
    matrix.update()
    time.sleep(5)

def clear_pixels(pixels):
    for i in range(len(pixels)):
        for j in range(len(pixels[i])):
            pixels[i][j] = BLACK

def get_input():
    global key_pressed
    global listen
    found = True

    while found:
        if listen:
            key = sys.stdin.buffer.read(1)[0]
            if key == 100:
                key_pressed['d'] = True
                found = False
    
def main():
    global listen
    
    try:
        matrix = Matrix_Update()
        splash = Custom_Shape(8, 15, matrix.pixels, 'WallBall/splash.csv')
        filedescriptors = termios.tcgetattr(sys.stdin)
        tty.setcbreak(sys.stdin)
        
        run = True

        title = [[]]

        clock = Clock(FPS)

        t = threading.Thread(target=get_input, daemon=True)
        t.start()
        while run:
            clock.tick()

            if key_pressed['d']:
                t.join()
                listen = False
                clear_pixels(matrix.pixels)
                score, run = gameLogic.play_game(matrix, clock)
                clear_pixels(matrix.pixels)
                show_score(score, matrix)
                clear_pixels(matrix.pixels)
                key_pressed['d'] = False
                t = threading.Thread(target=get_input, daemon=True)
                t.start()
                
            splash.draw()
            matrix.update()
            
            if not listen:
                listen = True
    except KeyboardInterrupt as e:
        print("Done")
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, filedescriptors)



if __name__ == '__main__':
    main()
