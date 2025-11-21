# Stepick.org — Python. Часть 4
# Практическая работа № 2


# pylint: disable=W0105


# === Задача 1 ===
"""
Вывести подстроку с индекса 1 до последнего символа.
"""


def m_4_2_1(data: str, start=1):
    return data[start:]


# print(m_4_2_1(input()))


# === Задача 2 ===
"""
    Вывести символы, начиная с первого и заканчивая на “o” (ее не выводить)
    """


def m_4_2_2(data: str, start=0, ch="o"):
    end = data.index(ch) if ch in data else None
    return data[start:end]


# print(m_4_2_2(input()))


# === Задача 4 ===
"""
    Вывести все символы после первого вхождения символа “o”
    (включая символ) либо "'o' not found"
    """


def m_4_2_4(data: str, ch="o"):
    if ch in data:
        return data[data.index(ch) :]
    return "not found"


# print(m_4_2_4(input()))


# === Задача 5 ===
"""
    Выведите строку из первых четырех символов.
    Если длина строки меньше четырех, выведите всю строку.
    """


def m_4_2_5(data: str, count=4):
    return data[:count]


# print(m_4_2_5(input()))

# === Задача 6 ===
"""
    Выведите последний символ строки. Если строка пустая, выведите символ “a”.
    """


def m_4_2_6(data: str, i=-1):
    if data:
        return data[i]
    return "a"


# print(m_4_2_6(input()))
