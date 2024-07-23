from fibonacci_calculator.main import get_fibonacci_number, CALCULATION_TIMEOUT
import pytest


def test_fibonacci_zero():
    """Unit тест для функции get_fibonacci_number c n = 0"""
    with pytest.raises(RecursionError) as exc_info:
        get_fibonacci_number(0)
    assert str(exc_info.value) == 'Число n должно быть больше 0.'


def test_fibonacci_one():
    """Unit тест для функции get_fibonacci_number c n = 1"""
    assert get_fibonacci_number(1) == 1


def test_fibonacci_five():
    """Unit тест для функции get_fibonacci_number c n = 5"""
    assert get_fibonacci_number(5) == 8


def test_fibonacci_nine():
    """Unit тест для функции get_fibonacci_number c n = 9"""
    assert get_fibonacci_number(9) == 55


def test_fibonacci_large_number():
    """Unit тест для функции get_fibonacci_number c n = 36"""
    assert get_fibonacci_number(36) == 24157817


def test_test_fibonacci_huge_number():
    """Unit тест для функции get_fibonacci_number c n = 5000000000000"""
    with pytest.raises(TimeoutError) as exc_info:
        get_fibonacci_number(5000000000000)
    assert str(exc_info.value) == f"Превышен timeout вычисления числа " \
                                  f"fibonacci {CALCULATION_TIMEOUT} секунд."
