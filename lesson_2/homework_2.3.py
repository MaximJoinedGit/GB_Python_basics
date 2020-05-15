"""
3. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень). Напишите решения через list и через dict.
"""

# Ввод данных и проверка условия, что это число и оно от 1 до 12.
while True:
    month = input('Введите месяц цифрой: ')
    if month.isdigit() and 0 < int(month) < 13:
        break
    else:
        print('Такого месяца нет :)')

# Решение с использованием типа данных dict:
four_seasons_dict = {'Winter': ('12', '1', '2'), 'Spring': ('3', '4', '5'), 'Summer': ('6', '7', '8'),
                     'Autumn': ('9', '10', '11')}
for season, month_num in four_seasons_dict.items():
    if month in month_num:
        print(season)
        break

# Решение с использованием типа данных list:
four_seasons_list = ['12', 'Winter', '1', 'Winter', '2', 'Winter', '3', 'Spring', '4', 'Spring', '5', 'Spring', '6',
                     'Summer', '7', 'Summer', '8', 'Summer', '9', 'Autumn', '10', 'Autumn', '11', 'Autumn']
if month in four_seasons_list:
    month_in_list = four_seasons_list.index(month)
    print(four_seasons_list[month_in_list + 1])
