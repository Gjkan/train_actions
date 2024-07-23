# train_actions
Небольшой проект за 5 минут для изучения actions.

Структура проекта:
1. Модуль fibonacci_calculator:
   - вычисляет содержит функцию get_fibonacci_number, которая вычисляет числа Фибоначчи,
   - переменная CALCULATION_TIMEOUT задаёт timeout для вычислений, 
   - функция get_fibonacci_number вычисляет числа Фибоначчи для чисел > 0 (искусственный случай для расширения тест-кейсов).
2. Модуль tests:
   - содержит 6 unit тестов, тестирующих функцию get_fibonacci_number модуля fibonacci_calculator,
   - запускается командой pytest.
3. Workflows:
    - папка .github/workflows содержит один workflow run_unit_tests.yml,
    - run_unit_tests.yml основан на workflow 'Python application'
    - workflow при пуше с ветку main:
      - настраивает python на ubuntu;
      - устанавливает зависимости python из requirements.txt, если он есть;
      - производит линтинг с помощью flake8;
      - запускает unit тесты с помощью pytest.