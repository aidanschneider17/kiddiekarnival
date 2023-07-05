import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0 , 255)

ZERO = [[1, 1, 1],
        [1, 0, 1],
        [1, 0, 1],
        [1, 0, 1],
        [1, 1, 1]]

ONE =  [[0, 0, 1],
        [0, 0, 1],
        [0, 0, 1],
        [0, 0, 1],
        [0, 0, 1]]

TWO =  [[1, 1, 1],
        [0, 0, 1],
        [1, 1, 1],
        [1, 0, 0],
        [1, 1, 1]]

THREE =[[1, 1, 1],
        [0, 0, 1],
        [1, 1, 1],
        [0, 0, 1],
        [1, 1, 1]]

FOUR = [[1, 0, 1],
        [1, 0, 1],
        [1, 1, 1],
        [0, 0, 1],
        [0, 0, 1]]

FIVE = [[1, 1, 1],
        [1, 0, 0],
        [1, 1, 1],
        [0, 0, 1],
        [1, 1, 1]]

SIX =  [[1, 1, 1],
        [1, 0, 0],
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1]]

SEVEN = [[1, 1, 1],
         [0, 0, 1],
         [0, 0, 1],
         [0, 0, 1],
         [0, 0, 1]]

EIGHT = [[1, 1, 1],
         [1, 0, 1],
         [1, 1, 1],
         [1, 0, 1],
         [1, 1, 1]]

NINE = [[1, 1, 1],
        [1, 0, 1],
        [1, 1, 1],
        [0, 0, 1],
        [1, 1, 1]]

numbers = [ZERO, ONE, TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE]


class Pixel:
    def __init__(self, x, y, size, color, win):
        self._rect = pygame.Rect(x, y, size, size)
        self._color = color
        self._win = win

    @property
    def x(self):
        return self._rect.x

    @property
    def y(self):
        return self._rect.y

    @property
    def color(self):
        return self._color

    @x.setter
    def x(self, x):
        self._x = x

    @y.setter
    def y(self, y):
        self._y = y

    @color.setter
    def color(self, color):
        self._color = color

    def draw(self):
        pygame.draw.rect(self._win, self._color, self._rect)

class Game_Element:
    def __init__(self, x, y, width, height, color, pixels, direction, score=0):
        self._x = x
        self._y = y
        self._width = width
        self._height = height
        self._color = color
        self._pixels = pixels
        self._direction = direction
        self._score = 0

    @property
    def x(self):
        return self._x
    
    @property
    def y(self):
        return self._y

    @property
    def width(self):
        return self._width
    
    @property
    def height(self):
        return self._height
    
    
    @property
    def color(self):
        return self._color

    @property
    def direction(self):
        return self._direction

    @property
    def score(self):
        return self._score

    @x.setter
    def x(self, x):
        self._x = x

    @y.setter
    def y(self, y):
        self._y = y

    @direction.setter
    def direction(self, direction):
        self._direction = direction

    @score.setter
    def score(self, score):
        self._score = score
    
    
    def move(self):
        if self._direction == None:
            self.__draw(0, 0)
        else:
            if self._x == 0:
                self.__draw(len(self._pixels)//2, len(self._pixels)//2 - self._y)
                self._direction = [1, 0]
            elif self._x + self._width == len(self._pixels):
                self.__draw(-len(self._pixels)//2, len(self._pixels)//2)
                self._direction = [-1, 0]
            elif self._y == 0 or self._y == len(self._pixels) - self._height:
                self._direction[1] = self._direction[1] * -1
            
            self.__draw(self._direction[0], self._direction[1])

    def __draw(self, x_add, y_add):
        for i in range(self._width):
            for j in range(self._height):
                self._pixels[self._y+j][self._x+i].color = BLACK
        self._x += x_add
        self._y += y_add
        for i in range(self._width):
            for j in range(self._height):
                self._pixels[self._y+j][self._x+i].color = self._color

    def custom_move(self, direction):
        if direction == 'n' and self._y != 0:
            self.__draw(0, -1)
        elif direction == 's' and self._y != len(self._pixels) - self._height:
            self.__draw(0, 1)
        elif direction == 'e' and self._x != len(self._pixels) - self._width:
            self.__draw(1, 0)
        elif direction == 'w' and self._x != 0:
            self.__draw(-1, 0)

    
class Number:

    def __init__(self, x, y, color, pixels, num=0):
        self._x = x
        self._y = y
        self._color = color
        self._pixels = pixels
        self._num = 0
        self._num_shape = numbers[num]

    @property
    def x(self):
        return self._x
    
    @property
    def y(self):
        return self._y

    @property
    def num(self):
        return self._num

    @num.setter
    def num(self, num):
        self._num = num
        self.draw()
    
    def draw(self):
        x = self._x
        y = self._y

        for i in range(len(self._num_shape)):
            for j in range(len(self._num_shape[i])):
                if self._num_shape[i][j] == 1:
                    self._pixels[y+i][x+j].color = self._color
                elif self._num_shape[i][j] == 0:
                    self._pixels[y+i][x+j].color = BLACK

