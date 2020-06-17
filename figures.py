"""Модуль с методами геометрических фигур"""
import math


class Figure:
    """Общий Класс с методами для геометрических фигур"""

    name = None
    angles = None
    perimeter = None
    area = None

    def __init__(self, name, angles):
        """Конструктор с полями общего класса"""
        self.name = name
        self.angles = angles

    def get_name(self):
        """Метод возвращает имя фигуры"""
        return self.name

    def get_angles(self):
        """Метод возвращает угол(лы) фигуры"""
        return self.angles

    def add_area(self, another_figure):
        """Метод возвращает сумму площадей заданных фигур"""
        if isinstance(another_figure, Figure):
            sum_figures = self.area() + another_figure.area()
            return sum_figures
        else:
            raise AttributeError('Неправильный класс геометрической фигуры')


class Triangle(Figure):
    """Класс с методами для треугольника"""

    def __init__(self, a, b):
        """Переопределение полей конструктора класса треугольник"""
        super().__init__(name='Triangle', angles=3)
        self.a = a
        self.b = b

    def find_perimeter(self):
        """Метод поиска периметра фигуры"""
        c = math.sqrt(self.a ** 2 + self.b ** 2)
        perimeter = self.a + self.b + c
        return perimeter

    def find_area(self):
        """Метод поиска площади фигуры"""
        area = 0.5 * self.a * self.b
        return area


class Rectangle(Figure):
    """Класс с методами для прямоугольника"""

    def __init__(self, a, b):
        """Переопределение полей конструктора класса прямоугольник"""
        super().__init__(name='Rectangle', angles=4)
        self.a = a
        self.b = b
        if a == b:
            raise ValueError('Одна сторона фигуры должна быть больше другой')

    def find_perimeter(self):
        """Метод поиска периметра фигуры"""
        perimeter = 2 * self.a + 2 * self.b
        return perimeter

    def find_area(self):
        """Метод поиска площади фигуры"""
        area = self.a * self.b
        return area


class Square(Figure):
    """Класс с методами для квадрата"""

    def __init__(self, a):
        """Переопределение полей конструктора класса квадрат"""
        super().__init__(name='Square', angles=4)
        self.a = a

    def find_perimeter(self):
        """Метод поиска периметра фигуры"""
        perimeter = 4 * self.a
        return perimeter

    def find_area(self):
        """Метод поиска площади фигуры"""
        area = self.a ** 2
        return area


class Circle(Figure):
    """Класс с методами для окружности"""

    def __init__(self, radius):
        """Переопределение полей конструктора класса окружность"""
        super().__init__(name='Circle', angles=0)
        self.radius = radius

    def find_perimeter(self):
        """Метод поиска периметра фигуры"""
        perimeter = self.radius * 2 * math.pi
        return perimeter

    def find_area(self):
        """Метод поиска площади фигуры"""
        area = self.radius ** 2 * math.pi
        return area