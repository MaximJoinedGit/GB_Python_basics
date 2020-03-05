"""
1. Поработайте с переменными, создайте несколько, выведите на экран, запросите у пользователя несколько чисел и строк
и сохраните в переменные, выведите на экран.
"""

var_int = 1
var_str = 'Your variables:'
var_float = 1.0
var_bool = (type(var_int) == int)
var_another_str = 'Baden'

print(var_str, var_int, var_float, var_bool, sep='\n')
print('Sep=\'\' doesn\'t work with sities. For example: ', var_another_str * (int(var_bool) + int(var_float)),
      sep='city ')

from_user_1 = input('Enter numbers, letters or words: ')
from_user_2 = input('Enter a bit more: ')
from_user_3 = input('One last time: ')
print(f'You entered:\n{from_user_1}\n{from_user_2}\n{from_user_3}')
