"""
5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

with open('homework_5.5.txt', 'w', encoding='utf-8') as w:
    while True:
        user_input = input('Введите числа через пробел: ')
        try:
            list(map(int, user_input.split()))
        except ValueError:
            print('В строке, которую вы ввели было не число! Повторите ввод.')
        else:
            w.write(user_input)
            break
with open('homework_5.5.txt', 'r', encoding='utf-8') as r:
    print(sum(map(int, r.readline().split())))
