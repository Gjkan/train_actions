from time import time

CALCULATION_TIMEOUT = 15


def get_fibonacci_number(n: int) -> int:
    """
    Функция возвращает число Фибоначчи.
     Параметр:
                    n (int): порядковый номер числа Фибоначчи.
     Возвращаемое значение:
                    fib_2 (int): число Фибоначчи с порядковым номером n.

    Если n == 0, то возбуждается исключение ValueError.
    Если вычисление числа Фибоначчи занимает больше CALCULATION_TIMEOUT секунд, возбуждается исключение TimeoutError.
    """
    start_time = time()
    if n == 0:
        raise ValueError('Число n должно быть больше 0.')
    else:
        fib1 = 0
        fib2 = 1
        while n > 0:
            fib1, fib2 = fib2, fib1 + fib2
            n -= 1
            if (time() - start_time) > CALCULATION_TIMEOUT:
                raise TimeoutError(f"Превышен timeout вычисления числа fibonacci {CALCULATION_TIMEOUT} секунд.")
        return fib2
