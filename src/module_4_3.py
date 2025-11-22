# Stepick.org — Python. Часть 4
# Практическая работа № 3

# pylint: disable=W0105


# === Задача 1 ===
"""
Дано число n и строка с Пользовательским текстом.
    Выведи заметку, которую добавил Пользователь.
"""

# from sys import stdin


def m_4_3_1(data: str):
    num, text = data.strip().split("\n")
    return text[: int(num)]


# print(m_4_3_1(stdin.read()))


# === Задача 2 ===
"""
    Дана строка. Выведи часть текста в том виде, как она хранится у
    Пользователя в первом документе: каждый третий символ строки.
    """


def m_4_3_2(text: str, num=3):
    return text[num - 1 :: num]


# print(m_4_3_2(input()))


# === Задача 3 ===
"""
    Пользователь считает, что по индексу index в string стоит символ s.
    Прав ли он? Выведи "ДА" или "НЕТ".
    Дано такое число index, что символ по нему всегда найдётся.
    """

# from sys import stdin


def m_4_3_3(data: str):
    string, ch, index = data.strip().split("\n")
    if not index.isdigit() and ch.isdigit():
        ch, index = index, ch  # ошибка в тестах на платформе
    index = int(index)
    if index >= len(string):
        return "НЕТ"
    if string[index] == ch:
        return "ДА"
    return "НЕТ"


# print(m_4_3_3(stdin.read()))
