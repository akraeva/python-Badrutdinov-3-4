# Stepick.org — Python. Часть 3
# Практическая работа № 1


# pylint: disable=W0105


# === Задача 1 ===
"""
Напишите программу, которая выводит все четные числа от 1 до 10.
"""


def m_3_1_1(start=1, end=10):
    if end < start:
        return ""
    result = [num for num in range(start, end + 1) if num % 2 == 0]
    return "\n".join(map(str, result))


# print(m_3_1_1())


# === Задача 2 ===
"""
    Напишите программу, которая выводит квадраты чисел от 1 до 5.
    """


def m_3_1_2(start=1, end=5):
    if end < start:
        return ""
    result = [num**2 for num in range(start, end + 1)]
    return "\n".join(map(str, result))


# print(m_3_1_2())


# === Задача 3 ===
"""
    Напишите программу, которая выводит сумму всех чисел от 1 до 10.
    """


def m_3_1_3(start=1, end=10):
    if end < start:
        return 0
    result = sum(range(start, end + 1))
    return result


# print(m_3_1_3())


# === Задача 4 ===
"""
    Напишите программу, которая выводит все
    числа от 10 до 1 в обратном порядке.
    """


def m_3_1_4(start=1, end=10):
    if end < start:
        return ""
    result = [num for num in range(start, end + 1)][::-1]
    return "\n".join(map(str, result))


# print(m_3_1_4())


# === Задача 5 ===
"""
    Напишите программу, которая выводит все числа от 1 до 20, кратные 3.
    """


def m_3_1_5(start=1, end=20, div=3):
    if end < start:
        return ""
    result = [num for num in range(start, end + 1) if num % div == 0]
    return "\n".join(map(str, result))


# print(m_3_1_5())
