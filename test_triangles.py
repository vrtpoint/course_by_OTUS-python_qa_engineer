"""Модуль с тестами для треугольника"""
from source.figures import Triangle
import pytest


def test_create_triangle():
    """Тест создания треугольника"""
    triangle = Triangle(a=10, b=12)
    assert triangle.name == 'Triangle'

def test_triangle_perimeter():
    """Тест вычисления периметра треугольника"""
    triangle = Triangle(a=5, b=6)
    assert triangle.perimeter() == 18

def test_triangle_area():
    """Тест вычисления площади треугольника"""
    triangle = Triangle(a=5, b=6)
    assert triangle.area() == 15

def test_add_areas():
    """Тест вычисления суммы площадей двух фигур"""
    triangle = Triangle(a=5, b=6)
    assert triangle.add_area(triangle) == 30

def test_add_areas_error():
    """Тест вызова исключения с невалидными параметрами"""
    var = 10
    triangle = Triangle(a=5, b=6)
    with pytest.raises(AttributeError):
        triangle.add_area(var)
