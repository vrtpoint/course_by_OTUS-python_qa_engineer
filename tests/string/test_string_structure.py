"""Тесты структуры данных: string"""
import pytest


#Тест проверки длины фразы
def test_length_of_phrase(сreate_phrase):
    print(len(сreate_phrase))

#Тест проверки корректности сложения двух частей фразы в одну
def test_concatenation_phrase(сoncatenate_phrase):
    print(сoncatenate_phrase)
    assert сoncatenate_phrase == "Pytest - тестовый фреймворк"

#Тест сравнения типов данных фраз
@pytest.mark.parametrize('phrase', ["Pytest - тестовый фреймворк"])
def test_comparison_types(сreate_phrase, phrase):
    assert type(сreate_phrase) == type(phrase)

#Тест корректности среза фразы
def test_trimming_phrase(сreate_phrase):
    assert сreate_phrase[:6] == "Pytest"

#Тест положения регистра фразы
def test_upper_case(сreate_phrase):
    assert сreate_phrase.upper() == "PYTEST - ТЕСТОВЫЙ ФРЕЙМВОРК"
