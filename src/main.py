import pygame
from objects import *
from timekeeping import *

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

def handle_ball(ball, paddle, pixels_length, left_score, right_score):
    x_direction = None

    if ball.x == 0 and paddle.x == 0:
        paddle.score += 1
        left_score.num = paddle.score

    elif ball.x + ball.width == pixels_length and paddle.x + paddle.width == pixels_length:
        paddle.score += 1
        right_score.num = paddle.score

    elif (ball.x + ball.width == paddle.x or ball.x == paddle.x + paddle.width) and \
        ball.y >= paddle.y and ball.y + ball.height <= paddle.y + paddle.height:
        if paddle.x == 0:
            x_direction = 1
        else:
            x_direction = -1

        if ball.y < paddle.y + (paddle.height / 4):
            ball.direction = [x_direction, -2]
        elif ball.y < paddle.y + (paddle.height / 2):
            ball.direction = [x_direction, -1]
        elif ball.y < paddle.y + (paddle.height / 4 * 3):
            ball.direction = [x_direction, 1]
        else:
            ball.direction = [x_direction, 2]


def handle_paddles(left_paddle, right_paddle, keys_pressed):
    if keys_pressed[pygame.K_UP]:
        right_paddle.custom_move('n')
    if keys_pressed[pygame.K_DOWN]:
        right_paddle.custom_move('s')
    if keys_pressed[pygame.K_w]:
        left_paddle.custom_move('n')
    if keys_pressed[pygame.K_s]:
        left_paddle.custom_move('s')

def handle_win(ball, left_paddle, right_paddle):
    return not left_paddle.score == 5 or right_paddle.score == 5

def draw_window(pixels):
    for i in range(len(pixels)):
        for j in range(len(pixels)):
            pixels[i][j].draw()

    pygame.display.update()

def main():
    pixels = set_pixels()
    ball = Game_Element(len(pixels)//2, len(pixels)//2, 2, 2, RED, pixels, [1, 0])
    right_paddle = Game_Element(len(pixels)-2, len(pixels)//2, 2, 16, BLUE, pixels, None)
    left_paddle = Game_Element(0, len(pixels)//2, 2, 16, BLUE, pixels, None)
    left_paddle.custom_move('n')
    right_paddle.custom_move('n')
    left_score = Number(len(pixels)//2-7, 0, WHITE, pixels, 0)
    right_score = Number(len(pixels)//2+3, 0, WHITE, pixels, 0)
    left_score.draw()
    right_score.draw()

    clock = Clock(FPS)
    move_timer = Timer(FPS, 0.1)
    run = True
    while run:
        clock.tick()
        move_timer.tick()

        run = handle_win(ball, left_paddle, right_paddle)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys_pressed = pygame.key.get_pressed()

        if move_timer.completed:
            handle_paddles(left_paddle, right_paddle, keys_pressed)
            handle_ball(ball, left_paddle, len(pixels), left_score, right_score)
            handle_ball(ball, right_paddle, len(pixels), left_score, right_score)
            left_score.draw()
            right_score.draw()
            ball.move()
            left_paddle.move()
            right_paddle.move()
            move_timer.reset()

        draw_window(pixels)

    pygame.quit()


if __name__ == '__main__':
    main()