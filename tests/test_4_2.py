# Stepick.org — Python. Часть 4
# Практическая работа № 2

import pytest
from src.module_4_2 import (
    m_4_2_1,
    m_4_2_2,
    m_4_2_4,
    m_4_2_5,
    m_4_2_6,
)


# === Тесты для задачи 1 ===
@pytest.mark.parametrize(
    "data, start, expected",
    [
        ("Python", 1, "ython"),  # базовый случай
        ("Hello", 0, "Hello"),  # start = 0
        ("A", 1, ""),  # строка длина 1
        ("", 1, ""),  # пустая строка
    ],
)
def test_4_2_1(data, start, expected):
    assert m_4_2_1(data, start) == expected


# === Тесты для задачи 2 ===
@pytest.mark.parametrize(
    "data, start, ch, expected",
    [
        ("Hello world", 0, "o", "Hell"),  # базовый пример
        ("Python", 1, "o", "yth"),  # начало с индекса 1
        ("abc", 0, "x", "abc"),  # символ не найден
        ("foobar", 0, "o", "f"),  # первый символ совпадает
    ],
)
def test_4_2_2(data, start, ch, expected):
    assert m_4_2_2(data, start, ch) == expected


# === Тесты для задачи 4 ===
@pytest.mark.parametrize(
    "data, ch, expected",
    [
        ("Hello world", "o", "o world"),  # базовый случай
        ("Python", "P", "Python"),  # первый символ совпадает
        ("abc", "x", "not found"),  # символ отсутствует
        ("", "o", "not found"),  # пустая строка
    ],
)
def test_4_2_4(data, ch, expected):
    assert m_4_2_4(data, ch) == expected


# === Тесты для задачи 5 ===
@pytest.mark.parametrize(
    "data, count, expected",
    [
        ("Python", 4, "Pyth"),  # обычный случай
        ("abc", 4, "abc"),  # длина < count
        ("", 4, ""),  # пустая строка
        ("HelloWorld", 2, "He"),  # count < длины
    ],
)
def test_4_2_5(data, count, expected):
    assert m_4_2_5(data, count) == expected


# === Тесты для задачи 6 ===
@pytest.mark.parametrize(
    "data, i, expected",
    [
        ("Python", -1, "n"),  # последний символ
        ("A", -1, "A"),  # строка длина 1
        ("", -1, "a"),  # пустая строка
        ("Hello", 0, "H"),  # индекс 0
    ],
)
def test_4_2_6(data, i, expected):
    assert m_4_2_6(data, i) == expected
