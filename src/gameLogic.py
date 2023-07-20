import pygame
from objects import *
from timekeeping import *
import time
import random

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0 , 255)
GREEN = (0, 255, 0)

WINNER = 1

def handle_ball(ball, paddle, wall, pixels_length, score, ball_timer):
    x_direction = None

    if ball.x == wall.x + wall.width:
        x_direction = 1
        ball.direction = [x_direction, random.randint(-4, 4)]
        ball_timer.seconds = ball_timer.seconds - 0.01
        
    elif ball.x + ball.width == pixels_length:
        wall.score += 1

    elif ball.x + ball.width == paddle.x and \
        ball.y + 1 >= paddle.y and ball.y + ball.height - 2 <= paddle.y + paddle.height:
        x_direction = -1

        paddle.score += 1
        score.num = paddle.score

        if ball.y < paddle.y + (paddle.height / 4):
            ball.direction = [x_direction, -2]
        elif ball.y < paddle.y + (paddle.height / 2):
            ball.direction = [x_direction, -1]
        elif ball.y < paddle.y + (paddle.height / 4 * 3):
            ball.direction = [x_direction, 1]
        else:
            ball.direction = [x_direction, 2]


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


def start_animation(pixels):
    countdown = Number(len(pixels)//2-1, len(pixels)//2-6, WHITE, pixels, num=3)
    while countdown.num > 0:
        countdown.draw()
        draw_window(pixels)
        time.sleep(1)
        countdown.num -= 1

    countdown.delete()


def play_game(pixels, clock):
    ball = Game_Element(len(pixels)//2, len(pixels)//2, 2, 2, RED, pixels, [1, 0])
    paddle = Game_Element(len(pixels)-2, len(pixels)//2, 2, 16, BLUE, pixels, None)
    wall = Game_Element(0, 0, 2, 64, GREEN, pixels, None)
    paddle.custom_move('n')
    score = Number(len(pixels)//2-2, 0, WHITE, pixels)
    score.draw()

    ball_timer = Timer(clock.fps, 0.1)
    paddle_timer = Timer(clock.fps, 0.06)
    run = True
    end = True

    start_animation(pixels)

    while run:

        clock.tick()
        paddle_timer.tick()
        ball_timer.tick()

        run = wall.score == 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                end = False

        keys_pressed = pygame.key.get_pressed()

        if paddle_timer.completed and run:
            score.draw()
            paddle.move()
            paddle_timer.reset()
            handle_paddles(paddle, keys_pressed)

        if ball_timer.completed and run:
            ball.move()
            handle_ball(ball, paddle, wall, len(pixels), score, ball_timer)
            ball_timer.reset()

        draw_window(pixels)

    return paddle.score, end