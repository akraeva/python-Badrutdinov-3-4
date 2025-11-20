# Stepick.org — Python. Часть 4
# Практическая работа № 1

import pytest
from src.module_4_1 import m_4_1_1, m_4_1_2, m_4_1_3, m_4_1_4

# для запуска pytest -k "test_4_1_" -q -x --tb=short


# === Тесты для Задачи 1 ===


@pytest.mark.parametrize(
    "data, expected",
    [
        ("Python", "Pyt"),
        ("Hi", "Hi"),  # меньше трёх символов
        ("", ""),  # пустая строка
        ("abcde", "abc"),
    ],
)
def test_4_1_1(data, expected):
    assert m_4_1_1(data) == expected


# === Тесты для Задачи 2 ===
@pytest.mark.parametrize(
    "data, expected",
    [
        ("Python", "hon"),
        ("Hi", "Hi"),  # меньше трёх символов
        ("", ""),  # пустая строка
        ("abcde", "cde"),
    ],
)
def test_4_1_2(data, expected):
    assert m_4_1_2(data) == expected


# === Тесты для Задачи 3 ===
@pytest.mark.parametrize(
    "data, expected",
    [
        ("Python", "Python"),  # между первым и последним
        ("Hi", "Hi"),  # между первым и последним пусто
        ("abc", "abc"),  # только один символ между
        ("a", "a"),  # один символ в строке
        ("", ""),  # пустая строка
    ],
)
def test_4_1_3(data, expected):
    assert m_4_1_3(data) == expected


# === Тесты для Задачи 4 ===
@pytest.mark.parametrize(
    "data, expected",
    [
        ("Python", "hon"),
        ("abcdef", "def"),
        ("abc", ""),  # меньше четырёх символов
        ("a", ""),  # один символ
        ("", ""),  # пустая строка
    ],
)
def test_4_1_4(data, expected):
    assert m_4_1_4(data) == expected
