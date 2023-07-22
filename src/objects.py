from samplebase import SampleBase
import random

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
ORANGE = (255, 136, 0)
GREEN = (0, 255, 0)
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


class Matrix_Update(SampleBase):
    def __init__(self, *args, **kwargs):
        super(Matrix_Update, self).__init__(*args, **kwargs)
        self.process()

        self._canvas = self.matrix.CreateFrameCanvas()
        self._pixels = []

        for i in range(0, self.matrix.width):
            row = []
            for j in range(0, self.matrix.height):
                row.append(None)
            self._pixels.append(row)

    @property
    def pixels(self):
        return self._pixels

    def update(self):
        for y in range(len(self._pixels)):
            for x in range(len(self._pixels[y])):
                color = self._pixels[y][x]
                if color != None:
                    self._canvas.SetPixel(x, y, color[0], color[1], color[2])
        self._canvas = self.matrix.SwapOnVSync(self._canvas)
        

class Game_Element:
    def __init__(self, x, y, width, height, color, pixels, score=0):
        self._x = x
        self._y = y
        self._width = width
        self._height = height
        self._color = color
        self._pixels = pixels

        self.__draw(0, 0)

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

    @x.setter
    def x(self, x):
        self._x = x

    @y.setter
    def y(self, y):
        self._y = y
    
    def move(self):
        pass

    def control_move(self, direction):
        pass

    def __draw(self, x_add, y_add):
        if self._x + self._width + x_add > len(self._pixels):
            x_add = len(self._pixels) - (self._x + self._width)
        elif self._x + x_add < 0:
            x_add = 0 - self._x

        if self._y + self._height + y_add > len(self._pixels):
            y_add = len(self._pixels) - (self._y + self._height)
        elif self._y + y_add < 0:
            y_add = 0 - self._y

        for i in range(self._width):
            for j in range(self._height):
                self._pixels[self._y+j][self._x+i] = BLACK
        self._x += x_add
        self._y += y_add
        for i in range(self._width):
            for j in range(self._height):
                self._pixels[self._y+j][self._x+i] = self._color


class Ball(Game_Element):
    def __init__(self, x, y, width, height, color, pixels, direction):
        super().__init__(x, y, width, height, color, pixels)

        self._direction = direction

    @property
    def direction(self):
        return self._direction

    @direction.setter
    def direction(self, direction):
        self._direction = direction

    def move(self):
        if self._direction == None:
            self.__draw(0, 0)
        else:
            if self._x + self._width == len(self._pixels):
                self.__draw(-len(self._pixels)//2, len(self._pixels)//2 - self._y)
                self._direction = [1, 0]
            elif self._y == 0 or self._y == len(self._pixels) - self._height:
                self._direction[1] = self._direction[1] * -1
            
            self.__draw(self._direction[0], self._direction[1])


class Paddle(Game_Element):
    def __init__(self, x, y, width, height, color, pixels, score=0):
        super().__init__(x, y, width, height, color, pixels)

        self._score = score

    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self, score):
        self._score = score

    def control_move(self, direction):
        if direction == 'n' and self._y != 0:
            self.__draw(0, -1)
        elif direction == 's' and self._y != len(self._pixels) - self._height:
            self.__draw(0, 1)
        elif direction == 'e' and self._x != len(self._pixels) - self._width:
            self.__draw(1, 0)
        elif direction == 'w' and self._x != 0:
            self.__draw(-1, 0)


class Wall(Paddle):
    def __init__(self, x, y, width, height, color, pixels, score=0):
        super().__init__(x, y, width, height, color, pixels, score)
        self._angle = 0
        self.new_angle()

    @property
    def angle(self):
        return self._angle
    

    def new_angle(self):
        self._angle = random.randint(-4, 4)

        if self._angle == -4 or self._angle == 4:
            self._color = RED
        elif self._angle == -3 or self._angle == 3:
            self._color = ORANGE
        elif self._angle == -2 or self._angle == 2:
            self._color = YELLOW
        elif self._angle == -1 or self._angle == 1:
            self._color = GREEN
    
class Number(Game_Element):

    def __init__(self, x, y, color, pixels, num=0, num_shape=None):
        super().__init__(x, y, 0, 0, color, pixels)

        self._num = num

        if num_shape == None:
            self._num_shape = numbers[num]
        else:
            self._num_shape = num_shape
            self._num = None

    @property
    def num(self):
        return self._num

    @num.setter
    def num(self, num):
        self._num = num
        self._num_shape = numbers[num]
        self.draw()
    
    def draw(self):
        x = self._x
        y = self._y

        for i in range(len(self._num_shape)):
            for j in range(len(self._num_shape[i])):
                if self._num_shape[i][j] == 1:
                    self._pixels[y+i][x+j] = self._color
                elif self._num_shape[i][j] == 0:
                    self._pixels[y+i][x+j] = BLACK

    def delete(self):
        for i in range(len(self._num_shape)):
            for j in range(len(self._num_shape[i])):
                self._pixels[self._y+i][self._x+j] = BLACK
