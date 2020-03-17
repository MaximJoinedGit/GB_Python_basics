"""
7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
При вызове функции должен создаваться объект-генератор. Функция должна вызываться следующим образом: for el in fact(n).
Ф-я отвечает за получение факториала числа, а в цикле необходимо выводить только первые n чисел, начиная с 1! и до n!.
Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.
"""
from itertools import count


def fact(n):
    """
    Function returns every iteration of factorial.
    :param n: factorial number.
    :type n: int
    :return: factorial number step by step.
    """
    res = 1
    for i in count(1):
        if i > n:
            break
        else:
            res *= i
            yield res


for el in fact(9):
    print(el)
