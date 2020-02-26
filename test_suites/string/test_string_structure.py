"""Тесты структуры данных: string"""
import pytest


#Тест проверки длины фразы
def test_length_of_phrase(сreate_phrase):
    print(len(сreate_phrase))

#Тест проверки корректности сложения двух частей фразы в одну
def test_concatenation_phrase(сoncatenate_phrase):
    print(сoncatenate_phrase)
    assert сoncatenate_phrase == "Pytest - тестовый фреймворк"


