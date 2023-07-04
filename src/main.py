import pygame
from objects import *

WIDTH = 1300

WIN = pygame.display.set_mode((WIDTH, WIDTH))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0 , 255)

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

def handle_ball(ball, left_paddle):
    if ball.x + ball.width == left_paddle.x and ball.y >= left_paddle.y and ball.y + \
    ball.height <= left_paddle.y + left_paddle.height:
        if ball.y < (left_paddle.y + left_paddle.height) / 2:
            ball.direction = [-1, -1]
        else:
            ball.direction = [-1, 1]

def handle_paddles(left_paddle, keys_pressed):
    if keys_pressed[pygame.K_UP]:
        left_paddle.custom_move('n')
    elif keys_pressed[pygame.K_DOWN]:
        left_paddle.custom_move('s')

def draw_window(pixels):
    for i in range(len(pixels)):
        for j in range(len(pixels)):
            pixels[i][j].draw()

    pygame.display.update()

def main():
    pixels = set_pixels()
    ball = Game_Element(len(pixels)//2, len(pixels)//2, 2, 2, RED, pixels, [1, 0])
    left_paddle = Game_Element(len(pixels)-2, len(pixels)//2, 2, 8, BLUE, pixels, None)
    left_paddle.custom_move('n')

    clock = pygame.time.Clock()
    move_timer = Timer(FPS, 0.1)
    run = True
    while run:
        clock.tick(FPS)
        move_timer.tick()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys_pressed = pygame.key.get_pressed()

        if move_timer.completed:
            handle_paddles(left_paddle, keys_pressed)
            handle_ball(ball, left_paddle)
            ball.move()
            left_paddle.move()
            move_timer.reset()

        draw_window(pixels)

    pygame.quit()


if __name__ == '__main__':
    main()