import math
# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

class Triangle(object):
    x1: int
    y1: int
    x2: int
    y2: int
    x3: int
    y3: int
    square: float
    side_length: float
    height: float

    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.x1 = int(x1)
        self.y1 = int(y1)
        self.x2 = int(x2)
        self.y2 = int(y2)
        self.x3 = int(x3)
        self.y3 = int(y3)

    def get_tri_square(self):
        self.square = (1 / 2) * abs(((self.x2 - self.x1) * (self.y3 - self.y1))
                                             - ((self.x3 - self.x1) * (self.y2 - self.y1)))

    def get_tri_side_len(self):
        self.side_length = math.sqrt(((self.x2 - self.x1)**2) + ((self.y2 - self.y1)**2)) \
                                    + math.sqrt(((self.x3 - self.x2)**2) + ((self.y3 - self.y2)**2)) \
                                    + math.sqrt(((self.x3 - self.x1)**2) + ((self.y3 - self.y1)**2))

    def get_tri_height(self):
        self.get_tri_square()
        self.height = (2 * self.square) - math.sqrt(((self.x2 - self.x1)**2) + ((self.y2 - self.y1)**2))


triangle1 = Triangle(-1, -3, 3, 4, 5, -5)

triangle1.get_tri_square()
triangle1.get_tri_height()
triangle1.get_tri_side_len()
print(triangle1.square, triangle1.side_length, triangle1.height)



# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.
