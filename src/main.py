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

WINNER = 1

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

def handle_ball(ball, paddle, wall, pixels_length, left_score, right_score, ball_timer):
    x_direction = None
    score_change = False

    if ball.x == wall.x + wall.width:
        paddle.score += 1
        right_score.num = paddle.score
        x_direction = 1
        ball.direction = [x_direction, random.randint(-4, 4)]
        ball_timer.seconds = ball_timer.seconds / 8 * 7
        

    elif ball.x + ball.width == pixels_length and paddle.x + paddle.width == pixels_length:
        wall.score += 1
        left_score.num = paddle.score
        score_change = True

    elif ball.x + ball.width == paddle.x and \
        ball.y + 1 >= paddle.y and ball.y + ball.height - 2 <= paddle.y + paddle.height:
        x_direction = -1

        if ball.y < paddle.y + (paddle.height / 4):
            ball.direction = [x_direction, -2]
        elif ball.y < paddle.y + (paddle.height / 2):
            ball.direction = [x_direction, -1]
        elif ball.y < paddle.y + (paddle.height / 4 * 3):
            ball.direction = [x_direction, 1]
        else:
            ball.direction = [x_direction, 2]

    return score_change


def handle_paddles(paddle, keys_pressed):
    if keys_pressed[pygame.K_UP]:
        paddle.custom_move('n')
    if keys_pressed[pygame.K_DOWN]:
        paddle.custom_move('s')

def draw_window(pixels):
    for i in range(len(pixels)):
        for j in range(len(pixels)):
            pixels[i][j].draw()

    pygame.display.update()


def point_animation(pixels):
    print("here")
    countdown = Number(len(pixels)//2-1, len(pixels)//2-6, WHITE, pixels, num=3)
    print(countdown.num)
    while countdown.num > 0:
        countdown.draw()
        draw_window(pixels)
        time.sleep(1)
        countdown.num -= 1

    countdown.delete()


def play_game(pixels):
    ball = Game_Element(len(pixels)//2, len(pixels)//2, 2, 2, RED, pixels, [1, 0])
    paddle = Game_Element(len(pixels)-2, len(pixels)//2, 2, 16, BLUE, pixels, None)
    wall = Game_Element(0, 0, 2, 64, GREEN, pixels, None)
    paddle.custom_move('n')
    left_score = Number(len(pixels)//2-7, 0, WHITE, pixels)
    right_score = Number(len(pixels)//2+3, 0, WHITE, pixels)
    left_score.draw()
    right_score.draw()

    clock = Clock(FPS)
    ball_timer = Timer(FPS, 0.1)
    paddle_timer = Timer(FPS, 0.06)
    run = True
    end = True
    score_change = False
    while run:

        clock.tick()
        paddle_timer.tick()
        ball_timer.tick()

        run = not wall.score == WINNER

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                end = False

        keys_pressed = pygame.key.get_pressed()

        if paddle_timer.completed and run:
            left_score.draw()
            right_score.draw()
            paddle.move()
            paddle_timer.reset()
            handle_paddles(paddle, keys_pressed)

            if score_change:
                point_animation(pixels)
                score_change = False

        if ball_timer.completed and run:
            ball.move()
            score_change = handle_ball(ball, paddle, wall, len(pixels), left_score, right_score, ball_timer)
            ball_timer.reset()

        draw_window(pixels)

    return end


def clear_pixels(pixels):
    for i in range(len(pixels)):
        for j in range(len(pixels[i])):
            pixels[i][j].color = BLACK

    
def main():
    pixels = set_pixels()
    run = True

    title = [[]]

    while run:
        run = play_game(pixels)
        clear_pixels(pixels)

    pygame.quit()



if __name__ == '__main__':
    main()