"""Модуль с тестами для квадрата"""
from source.figures import Square
import pytest


def test_create_square():
    """Тест создания квадрата"""
    square = Square(a=10)
    assert square.name == 'Square'

def test_square_perimeter():
    """Тест вычисления периметра квадрата"""
    square = Square(a=10)
    assert square.perimeter() == 40

def test_square_area():
    """Тест вычисления площади четырехугольника"""
    square = Square(a=10)
    assert square.area() == 100

def test_add_areas():
    """Тест вычисления суммы площадей двух фигур"""
    square = Square(a=10)
    assert square.add_area(square) == 200

def test_add_areas_error():
    """Тест вызова исключения с невалидными параметрами"""
    var = 10
    square = Square(a=10)
    with pytest.raises(AttributeError):
        square.add_area(var)
