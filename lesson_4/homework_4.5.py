"""
5. Реализовать формирование списка, используя функцию range() и возможности генератора.
В список должны войти четные числа от 100 до 1000 (включая границы).
Необходимо получить результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce().
"""

from random import randint
from functools import reduce

nums = [randint(100, 1000) for num in range(10)]
even_nums = [x for x in nums if not x % 2]
mul = reduce(lambda x, y: x * y, even_nums)
print(mul)
