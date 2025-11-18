# Stepick.org — Python. Часть 3
# Практическая работа № 1


import pytest
from src.module_3_1 import m_3_1_1, m_3_1_2, m_3_1_3, m_3_1_4, m_3_1_5

# для запуска pytest -k "test_3_1_" -q -x --tb=short


# === Тест к задаче 1 ===


@pytest.mark.parametrize(
    "start, end, expected",
    [
        # Base sample test — default range 1..10
        pytest.param(1, 10, "2\n4\n6\n8\n10", id="default_range_1_to_10"),
        # Custom range — normal case
        pytest.param(1, 5, "2\n4", id="range_1_to_5"),
        # Custom range — even numbers inside range
        pytest.param(3, 12, "4\n6\n8\n10\n12", id="range_3_to_12"),
        # Range where start = end and it is even
        pytest.param(4, 4, "4", id="single_value_even"),
        # Range where start = end and it is odd
        pytest.param(5, 5, "", id="single_value_odd"),
        # No valid numbers (range inverted)
        pytest.param(10, 1, "", id="end_less_than_start"),
        # Range with no even numbers
        pytest.param(1, 1, "", id="no_even_numbers"),
    ],
)
def test_3_1_1(start, end, expected):
    assert m_3_1_1(start, end) == expected


# === Тест к задаче 2 ===


@pytest.mark.parametrize(
    "start, end, expected",
    [
        # Base sample test — default range 1..5
        pytest.param(1, 5, "1\n4\n9\n16\n25", id="default_range_1_to_5"),
        # Custom range — smaller range
        pytest.param(1, 3, "1\n4\n9", id="range_1_to_3"),
        # Custom range — larger range
        pytest.param(2, 6, "4\n9\n16\n25\n36", id="range_2_to_6"),
        # Single number — 4^2
        pytest.param(4, 4, "16", id="single_value"),
        # No values — inverted range
        pytest.param(6, 2, "", id="end_less_than_start"),
        # Range including negative numbers
        pytest.param(-2, 2, "4\n1\n0\n1\n4", id="range_negative_to_positive"),
        # Only negative range
        pytest.param(-4, -2, "16\n9\n4", id="negative_range"),
    ],
)
def test_3_1_2(start, end, expected):
    assert m_3_1_2(start, end) == expected


# === Тест к задаче 3 ===


@pytest.mark.parametrize(
    "start, end, expected",
    [
        # Base sample — sum 1..10
        pytest.param(1, 10, 55, id="default_range_1_to_10"),
        # Shorter range
        pytest.param(1, 5, 15, id="range_1_to_5"),
        # Custom range
        pytest.param(3, 7, 25, id="range_3_to_7"),
        # Single number
        pytest.param(4, 4, 4, id="single_number"),
        # Inverted range — no numbers
        pytest.param(10, 1, 0, id="end_less_than_start"),
        # Range with negative to positive
        pytest.param(-2, 3, 3, id="negative_to_positive"),
        # Fully negative range
        pytest.param(-5, -3, -12, id="negative_only"),
    ],
)
def test_3_1_3(start, end, expected):
    assert m_3_1_3(start, end) == expected


# === Тест к задаче 4 ===


@pytest.mark.parametrize(
    "start, end, expected",
    [
        # Base sample — 10..1
        pytest.param(
            1, 10, "10\n9\n8\n7\n6\n5\n4\n3\n2\n1", id="default_range_10_to_1"
        ),
        # Custom range — 5..1
        pytest.param(1, 5, "5\n4\n3\n2\n1", id="range_5_to_1"),
        # Custom range — 7..3
        pytest.param(3, 7, "7\n6\n5\n4\n3", id="range_7_to_3"),
        # Single number (start = end)
        pytest.param(4, 4, "4", id="single_number"),
        # Inverted range — produces empty output
        pytest.param(10, 1, "", id="start_less_than_end"),
        # Negative reversed range
        pytest.param(-4, -1, "-1\n-2\n-3\n-4", id="negative_descending"),
        # Mixed sign reversed range
        pytest.param(-1, 3, "3\n2\n1\n0\n-1", id="mixed_sign_descending"),
    ],
)
def test_3_1_4(start, end, expected):
    assert m_3_1_4(start, end) == expected


# === Тест к задаче 5 ===


@pytest.mark.parametrize(
    "start, end, div, expected",
    [
        # Базовый тест — как в условии
        pytest.param(1, 20, 3, "3\n6\n9\n12\n15\n18", id="default_1_20_div3"),
        # Другой диапазон
        pytest.param(1, 10, 3, "3\n6\n9", id="range_1_10_div3"),
        # Изменённый делитель
        pytest.param(1, 20, 4, "4\n8\n12\n16\n20", id="div4"),
        # Нет подходящих чисел
        pytest.param(1, 5, 7, "", id="no_multiples"),
        # Отрицательные числа
        pytest.param(-10, 10, 5, "-10\n-5\n0\n5\n10", id="negative_and_positive_div5"),
        # Смешанный диапазон с div=2
        pytest.param(-3, 3, 2, "-2\n0\n2", id="mixed_negative_positive"),
        # Некорректный диапазон (конец < начала)
        pytest.param(10, 1, 3, "", id="invalid_range"),
    ],
)
def test_3_1_5(start, end, div, expected):
    assert m_3_1_5(start, end, div) == expected
