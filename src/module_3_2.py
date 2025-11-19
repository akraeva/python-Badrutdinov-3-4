# Stepick.org — Python. Часть 3
# Практическая работа № 2


# pylint: disable=W0105


# === Задача 1 ===
"""
Напишите программу, которая выводит все числа от 1 до 100,
кратные как 3, так и 5.
"""


def m_3_2_1(start=1, end=100):
    if end < start:
        return ""
    result = [num for num in range(start, end + 1) if num % (3 * 5) == 0]
    return "\n".join(map(str, result))


# print(m_3_2_1())


# === Задача 2 ===
"""
    Напишите программу, которая выводит сумму кубов чисел от 1 до 5.
    """


def m_3_2_2(start=1, end=5):
    if end < start:
        return 0
    result = sum([num**3 for num in range(start, end + 1)])
    return result


# print(m_3_2_2())


# === Задача 3 ===
"""
    Напишите программу, которая выводит первые 10 чисел Фибоначчи.
    Числа Фибоначчи — это последовательность чисел, которые задаются
    по определённому правилу. Оно звучит так: каждое следующее число
    равно сумме двух предыдущих. Первые два числа заданы сразу и равны 1
    """


def m_3_2_3(count=10):
    if count < 1:
        return ""
    if count == 1:
        return "0"
    result = [0, 1]
    while len(result) < count:
        result.append(result[-1] + result[-2])
    return "\n".join(map(str, result))


# print(m_3_2_3())


# === Задача 4 ===
"""
    Напишите программу, которая выводит все простые числа от 1 до 20.
    """


def m_3_2_4(start=1, end=20):
    def is_prime(num):
        if num == 1:
            return False
        for div in range(2, int(num**0.5) + 1):
            if num % div == 0:
                return False
        return True

    result = [num for num in range(start, end + 1) if is_prime(num)]
    return "\n".join(map(str, result))


# print(m_3_2_4())


# === Задача 5 ===
"""
    Выведите все буквы в слове "Python".
    """


def m_3_2_5(word="Python"):
    result = list(word)
    return "\n".join(result)


# print(m_3_2_5())


# === Задача 6 ===
"""
    Выведите все числа от 1 до 20, кроме чисел 5 и 10.
    """


def m_3_2_6(start=1, end=20, ignore=(5, 10)):
    if end < start:
        return ""
    result = [num for num in range(start, end + 1) if num not in ignore]
    return "\n".join(map(str, result))


# print(m_3_2_6())


# === Задача 7 ===
"""
    Выведите все нечетные числа от 1 до 30.
    """


def m_3_2_7(start=1, end=30):
    if end < start:
        return ""
    result = [num for num in range(start, end + 1) if num % 2 == 1]
    return "\n".join(map(str, result))


# print(m_3_2_7())


# === Задача 8 ===
"""
    Посчитайте произведение всех чисел от 1 до 10.
    """


def m_3_2_8(start=1, end=10):
    if end < start:
        return ""
    result = [start]
    for num in range(start + 1, end + 1):
        result.append(result[-1] * num)
    return "\n".join(map(str, result))


# print(m_3_2_8())
