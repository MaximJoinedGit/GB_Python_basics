"""
4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. Для решения используйте цикл
while и арифметические операции.
"""

number = input()
loop_end = len(number)
i = 0
max_num = 0
if number.isdigit():
    while i < loop_end:
        number = int(number)
        temp = number % 10
        if temp > max_num:
            max_num = temp
        number //= 10
        i += 1
    print(max_num)
else:
    print('Вы ввели не число!')
