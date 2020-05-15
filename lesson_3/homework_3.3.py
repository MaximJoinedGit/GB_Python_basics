"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
"""


def my_func(*args):
    """
    Function to calculate the sum of two biggest numbers.
    :param args: 3 positional arguments.
    :type args: int
    :return: sum of the two biggest numbers.
    """
    result = sum(args) - min(args)
    return result


res = my_func(4, 1, 2)
print(res)
