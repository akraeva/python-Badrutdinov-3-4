# Stepick.org — Python. Часть 4
# Практическая работа № 3

import pytest
from src.module_4_3 import (
    m_4_3_1,
    m_4_3_2,
    m_4_3_3,
)


# === Тесты к задаче 1 ===
@pytest.mark.parametrize(
    "data, expected",
    [
        # Базовый пример из условия
        ("5\nфокус", "фокус"),
        # Обрезка строки
        ("3\nabcdef", "abc"),
        # n больше длины строки — вернуть всю строку
        ("10\nhi", "hi"),
        # n = 0 — пустая строка
        ("0\npython", ""),
        # В строке есть пробелы
        ("4\nhello world", "hell"),
        # Unicode
        ("2\nПривет", "Пр"),
    ],
)
def test_4_3_1(data, expected):
    assert m_4_3_1(data) == expected


# === Тесты к задаче 2 ===


@pytest.mark.parametrize(
    "text, num, expected",
    [
        # Из условия (хотя пример странный)
        ("Привет", 3, "ит"),
        # Каждый 2-й символ
        ("abcdef", 2, "bdf"),
        # Каждый 1-й символ — вся строка
        ("hello", 1, "hello"),
        # Длинный шаг
        ("abcdef", 10, ""),  # num=10 больше длины
        # Unicode
        ("Здравствуйте", 3, "рсуе"),
        # Пробелы тоже считаются символами
        ("a b c d", 2, "   "),
    ],
)
def test_4_3_2(text, num, expected):
    assert m_4_3_2(text, num) == expected


# === Тесты к задаче 3 ===


@pytest.mark.parametrize(
    "data, expected",
    [
        # Базовый тест из примера
        ("строка\nр\n2", "ДА"),
        # Неверный символ
        ("python\ny\n3", "НЕТ"),
        # Символ совпадает
        ("hello\nl\n2", "ДА"),
        # Индекс указывает на последний символ
        ("test\nt\n3", "ДА"),
        # Unicode
        ("привет\nв\n3", "ДА"),
        # Проверка индекса вне диапазона (ты добавила такую проверку)
        ("cat\nc\n10", "НЕТ"),
    ],
)
def test_4_3_3(data, expected):
    assert m_4_3_3(data) == expected
