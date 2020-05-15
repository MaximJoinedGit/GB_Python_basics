"""
4. Программа принимает действительное положительное число x и целое отрицательное число y.
Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без встроенной функции возведения числа в степень.

Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **.
Второй — более сложная реализация без оператора **, предусматривающая использование цикла.
"""


def my_func(x, y):
    """
    Recursive function. It takes two positional arguments calculates the result of negative exponentiation.
    :param x: first number.
    :type x: int
    :param y: second number.
    :type y: int
    :return: next iteration and exit from recursion.
    """
    return (1 / x) * my_func(x, y + 1) if y < -1 else 1 / x


res = my_func(3, -2)
print(res)
