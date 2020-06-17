"""Модуль с тестами для четырехугольника"""
from source.figures import Rectangle
import pytest


@pytest.mark.parametrize('a, b', [(10, 5), (5, 10), (10, 10)])
def test_create_rectangle_with_valid_values(a, b):
    """Тест создания четырехугольника"""
    if a > b:
        rectangle = Rectangle(a, b)
        assert rectangle.name == 'Rectangle'
    elif a < b:
        rectangle = Rectangle(a, b)
        assert rectangle.name == 'Rectangle'
    elif a == b:
        pytest.raises(ValueError)

def test_rectangle_perimeter():
    """Тест вычисления периметра четырехугольника"""
    rectangle = Rectangle(a=10, b=5)
    assert rectangle.perimeter() == 30

def test_rectangle_area():
    """Тест вычисления площади четырехугольника"""
    rectangle = Rectangle(a=10, b=5)
    assert rectangle.area() == 50

def test_add_areas():
    """Тест вычисления суммы площадей двух фигур"""
    rectangle = Rectangle(a=10, b=5)
    assert rectangle.add_area(rectangle) == 100

def test_add_areas_error():
    """Тест вызова исключения с невалидными параметрами"""
    var = 10
    rectangle = Rectangle(a=10, b=5)
    with pytest.raises(AttributeError):
        rectangle.add_area(var)
