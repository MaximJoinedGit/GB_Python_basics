"""
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля в качестве делителя программа
должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


class Zero(Exception):
    """
    class exception for ZeroDivizion error.
    """
    def __init__(self, text):
        self.text = text


res = None
while not res:
    first = input('Enter the divisible: ')
    second = input('Enter the divider: ')
    try:
        first = float(first)
        second = float(second)
        if second == 0:
            raise Zero('Zero division!')
    except ValueError:
        print('You entered not a number!')
    except Zero as z:
        print(z)
    else:
        res = first / second
        print(res)
