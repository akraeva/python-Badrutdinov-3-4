# Stepick.org — Python. Часть 3
# Практическая работа № 2


import pytest
from src.module_3_2 import (
    m_3_2_1,
    m_3_2_2,
    m_3_2_3,
    m_3_2_4,
    m_3_2_5,
    m_3_2_6,
    m_3_2_7,
    m_3_2_8,
)

# для запуска pytest -k "test_3_2_" -q -x --tb=short


# === Тест к задаче 1 ===


@pytest.mark.parametrize(
    "start, end, expected",
    [
        # Sample test — как в условии
        pytest.param(1, 100, "15\n30\n45\n60\n75\n90", id="default_1_100"),
        # Изменённый диапазон
        pytest.param(1, 50, "15\n30\n45", id="range_1_50"),
        # Узкий диапазон — одно кратное
        pytest.param(14, 16, "15", id="single_value_15"),
        # Диапазон без кратных
        pytest.param(1, 14, "", id="no_multiples"),
        # Отрицательный диапазон
        pytest.param(-50, 20, "-45\n-30\n-15\n0\n15", id="negative_range"),
        # Только отрицательные значения
        pytest.param(-100, -1, "- ninety…", id="only_negative"),
        # Перевёрнутый диапазон (конец < начала)
        pytest.param(10, 1, "", id="invalid_range"),
    ],
)
def test_3_2_1(start, end, expected):
    if expected == "- ninety…":
        expected = "\n".join(str(n) for n in range(-100, 0) if n % 15 == 0)

    assert m_3_2_1(start, end) == expected


# === Тест к задаче 2 ===


@pytest.mark.parametrize(
    "start, end, expected",
    [
        # Sample test
        pytest.param(1, 5, 225, id="sample_1_5"),
        # Один элемент диапазона
        pytest.param(3, 3, 27, id="single_value"),
        # Произвольный диапазон
        pytest.param(2, 4, 8 + 27 + 64, id="range_2_4"),
        # Отрицательные числа
        pytest.param(-3, -1, (-3) ** 3 + (-2) ** 3 + (-1) ** 3, id="negative_range"),
        # Диапазон через 0
        pytest.param(
            -2, 2, (-2) ** 3 + (-1) ** 3 + 0 + 1**3 + 2**3, id="range_through_zero"
        ),
        # Перевернутый диапазон
        pytest.param(10, 1, 0, id="invalid_range"),
        # Большие числа
        pytest.param(1, 10, sum(n**3 for n in range(1, 11)), id="big_range"),
    ],
)
def test_3_2_2(start, end, expected):
    assert m_3_2_2(start, end) == expected


# === Тест к задаче 3 ===


@pytest.mark.parametrize(
    "n, expected",
    [
        # Sample test — как в условии (первые 10 чисел)
        pytest.param(
            10,
            "0\n1\n1\n2\n3\n5\n8\n13\n21\n34",
            id="default_10_values",
        ),
        # n = 1
        pytest.param(1, "0", id="single_value"),
        # n = 2
        pytest.param(2, "0\n1", id="two_values"),
        # n = 5 — небольшой диапазон
        pytest.param(5, "0\n1\n1\n2\n3", id="five_values"),
        # n = 0 — пустой вывод
        pytest.param(0, "", id="zero_values"),
        # n = negative — ожидаем пустой вывод
        pytest.param(-5, "", id="negative_input"),
        # n = 15 — тест на расширенный диапазон
        pytest.param(
            15,
            "\n".join(
                [
                    "0",
                    "1",
                    "1",
                    "2",
                    "3",
                    "5",
                    "8",
                    "13",
                    "21",
                    "34",
                    "55",
                    "89",
                    "144",
                    "233",
                    "377",
                ]
            ),
            id="fifteen_values",
        ),
    ],
)
def test_3_2_3(n, expected):
    assert m_3_2_3(n) == expected


# === Тест к задаче 4 ===


@pytest.mark.parametrize(
    "start, end, expected",
    [
        # === Базовый тест из задания ===
        pytest.param(
            1,
            20,
            "2\n3\n5\n7\n11\n13\n17\n19",
            id="sample_range_1_20",
        ),
        # === Старт > конец — должен быть пустой вывод ===
        pytest.param(
            10,
            1,
            "",
            id="invalid_range_reverse",
        ),
        # === Диапазон внутри стандартного ===
        pytest.param(
            10,
            30,
            "11\n13\n17\n19\n23\n29",
            id="range_10_30",
        ),
        # === Минимальный диапазон без простых чисел ===
        pytest.param(
            1,
            1,
            "",
            id="range_with_no_primes",
        ),
        # === Диапазон с одним простым числом ===
        pytest.param(
            13,
            13,
            "13",
            id="single_prime",
        ),
        # === Большой диапазон (проверка корректности и производительности) ===
        pytest.param(
            1,
            50,
            "\n".join(
                [
                    "2",
                    "3",
                    "5",
                    "7",
                    "11",
                    "13",
                    "17",
                    "19",
                    "23",
                    "29",
                    "31",
                    "37",
                    "41",
                    "43",
                    "47",
                ]
            ),
            id="range_1_50",
        ),
    ],
)
def test_3_2_4(start, end, expected):
    assert m_3_2_4(start, end) == expected


# === Тест к задаче 5 ===


@pytest.mark.parametrize(
    "word, expected",
    [
        # === Базовый тест из задания ===
        pytest.param(
            "Python",
            "P\ny\nt\nh\no\nn",
            id="sample_python",
        ),
        # === Обычное слово ===
        pytest.param(
            "hello",
            "h\ne\nl\nl\no",
            id="word_hello",
        ),
        # === Однобуквенное слово ===
        pytest.param(
            "A",
            "A",
            id="single_letter",
        ),
        # === Пустая строка ===
        pytest.param(
            "",
            "",
            id="empty_string",
        ),
        # === Слово с пробелом ===
        pytest.param(
            "hi all",
            "h\ni\n \na\nl\nl",
            id="word_with_space",
        ),
        # === Unicode (русские буквы) ===
        pytest.param(
            "Привет",
            "П\nр\nи\nв\nе\nт",
            id="russian_word",
        ),
        # === Спецсимволы ===
        pytest.param(
            "!@#",
            "!\n@\n#",
            id="symbols",
        ),
    ],
)
def test_3_2_5(word, expected):
    assert m_3_2_5(word) == expected


# === Тест к задаче 6 ===


@pytest.mark.parametrize(
    "start, end, ignore, expected",
    [
        # === Базовый тест из задания ===
        pytest.param(
            1,
            20,
            (5, 10),
            "\n".join(
                [
                    "1",
                    "2",
                    "3",
                    "4",
                    "6",
                    "7",
                    "8",
                    "9",
                    "11",
                    "12",
                    "13",
                    "14",
                    "15",
                    "16",
                    "17",
                    "18",
                    "19",
                    "20",
                ]
            ),
            id="sample_range_1_20",
        ),
        # === Пустой список игнорируемых ===
        pytest.param(
            1,
            10,
            (),
            "\n".join(str(i) for i in range(1, 11)),
            id="no_ignored_values",
        ),
        # === Один игнорируемый элемент ===
        pytest.param(
            1,
            10,
            (3,),
            "\n".join(str(i) for i in range(1, 11) if i != 3),
            id="single_ignored",
        ),
        # === Несколько игнорируемых элементов, часть вне диапазона ===
        pytest.param(
            1,
            10,
            (3, 15, -1),
            "\n".join(str(i) for i in range(1, 11) if i not in {3}),
            id="ignored_outside_range",
        ),
        # === Полное исключение всех чисел ===
        pytest.param(
            1,
            5,
            (1, 2, 3, 4, 5),
            "",
            id="all_ignored",
        ),
        # === Диапазон в обратной стороне (start > end) ===
        pytest.param(
            10,
            1,
            (5,),
            "",
            id="invalid_range",
        ),
        # === Отрицательные значения диапазона ===
        pytest.param(
            -5,
            5,
            (0,),
            "\n".join(str(i) for i in range(-5, 6) if i != 0),
            id="range_with_negatives",
        ),
        # === Игнорируемые повторяются (дубликаты) ===
        pytest.param(
            1,
            10,
            (3, 3, 3),
            "\n".join(str(i) for i in range(1, 11) if i != 3),
            id="duplicate_ignored_values",
        ),
    ],
)
def test_3_2_6(start, end, ignore, expected):
    assert m_3_2_6(start, end, ignore) == expected


# === Тест к задаче 7 ===


@pytest.mark.parametrize(
    "start, end, expected",
    [
        # === Базовый тест из задания ===
        pytest.param(
            1,
            30,
            "\n".join(str(i) for i in range(1, 31) if i % 2 != 0),
            id="default_1_30",
        ),
        # === Только один нечетный элемент ===
        pytest.param(
            3,
            3,
            "3",
            id="single_odd",
        ),
        # === Нет нечетных чисел ===
        pytest.param(
            2,
            2,
            "",
            id="no_odds",
        ),
        # === Перевернутый диапазон (start > end) ===
        pytest.param(
            10,
            1,
            "",
            id="invalid_range",
        ),
        # === Диапазон с отрицательными числами ===
        pytest.param(
            -5,
            5,
            "\n".join(str(i) for i in range(-5, 6) if i % 2 != 0),
            id="negative_range",
        ),
        # === Диапазон полностью отрицательный ===
        pytest.param(
            -10,
            -1,
            "\n".join(str(i) for i in range(-10, 0) if i % 2 != 0),
            id="negative_only",
        ),
        # === Ограниченный диапазон с несколькими нечетными ===
        pytest.param(
            10,
            20,
            "\n".join(str(i) for i in range(10, 21) if i % 2 != 0),
            id="range_10_20",
        ),
    ],
)
def test_3_2_7(start, end, expected):
    assert m_3_2_7(start, end) == expected


# === Тест к задаче 8 ===


@pytest.mark.parametrize(
    "start, end, expected",
    [
        # === Базовый тест из задания ===
        pytest.param(
            1,
            10,
            "\n".join(
                [str(n) for n in [1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800]]
            ),
            id="default_1_10",
        ),
        # === Только один элемент диапазона ===
        pytest.param(
            5,
            5,
            "5",
            id="single_value",
        ),
        # === Небольшой диапазон ===
        pytest.param(
            1,
            5,
            "\n".join([str(n) for n in [1, 2, 6, 24, 120]]),
            id="range_1_5",
        ),
        # === Перевернутый диапазон (start > end) ===
        pytest.param(
            10,
            1,
            "",
            id="invalid_range",
        ),
        # === Диапазон с нулём ===
        pytest.param(
            0,
            5,
            "\n".join([str(n) for n in [0, 0, 0, 0, 0, 0]]),  # factorial with zero
            id="range_with_zero",
        ),
    ],
)
def test_3_2_8(start, end, expected):
    assert m_3_2_8(start, end) == expected
