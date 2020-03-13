"""
1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""


def division(numerator, denominator):
    """
    Function accepts two parameters, calculates the division and return the float value.
    :param numerator: any number.
    :type numerator: float
    :param denominator: any string number except zero.
    :type denominator: float
    :return: the result of the division.
    """
    result = None
    try:
        result = numerator / denominator
    except ZeroDivisionError:
        print('На ноль делить нельзя!')
    return result


def enter_digit(n):
    """
    Function accepts input from user, checks TypeError, converts string type to float type.
    :param n: the parameter describes to user what he should to enter.
    :type n: str
    :return: number converted to float type.
    """
    num = None
    while not type(num) == float:
        num = input(f'Введите {n}: ')
        try:
            num = float(num)
        except ValueError:
            print('Вы ввели не число. Повторите ввод!')
    return num


div = None
while not div:
    first = enter_digit('делимое')
    second = enter_digit('делитель')
    div = division(first, second)

print(div)
