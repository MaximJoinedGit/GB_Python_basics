"""
2. Для списка реализовать обмен значений соседних элементов,
т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().
"""

lst = input().split()
first_elem = 0
second_elem = 1
print(f'Список до: {lst}')
for i in range(len(lst) // 2):
    lst[first_elem], lst[second_elem] = lst[second_elem], lst[first_elem]
    first_elem += 2
    second_elem += 2
print(f'Список после: {lst}')
