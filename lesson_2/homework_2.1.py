"""
1. Создать список и заполнить его элементами различных типов данных.
Реализовать скрипт проверки типа данных каждого элемента. Использовать функцию type() для проверки типа.
Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.
"""

lst = [1, 1.2, 'text', True, False, (4, 5, 6), [7, 8, 9], {'a': 10, 'b': 11}]
for elem in lst:
    print(f'Элемент списка {elem}. Тип данных {type(elem)}')
