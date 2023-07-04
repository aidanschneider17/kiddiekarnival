import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0 , 255)

class Timer:
    def __init__(self, fps, seconds):
        self._tick_count = 0
        self._end_ticks = seconds * fps - 1
        self._completed = False

    @property
    def completed(self):
        return self._completed
    

    def tick(self):
        if not self._completed:
            self._tick_count += 1
            if self._tick_count == self._end_ticks:
                self._completed = True

    def reset(self):
        self._tick_count = 0
        self._completed = False

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
    def __init__(self, x, y, width, height, color, pixels, direction):
        self._x = x
        self._y = y
        self._width = width
        self._height = height
        self._color = color
        self._pixels = pixels
        self._direction = direction

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

    @x.setter
    def x(self, x):
        self._x = x

    @y.setter
    def y(self, y):
        self._y = y

    @direction.setter
    def direction(self, direction):
        self._direction = direction
    
    
    def move(self):
        if self._direction == None:
            self.__draw(0, 0)
        else:
            if self._x == 0 or self._x == len(self._pixels) - self._width:
                if self._direction == [1, 0]:
                    self._direction = [-1, 1]
                elif self._direction == [-1, 0]:
                    self._direction = [1, 1]
                else:
                    self._direction[0] = self._direction[0] * -1
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

    