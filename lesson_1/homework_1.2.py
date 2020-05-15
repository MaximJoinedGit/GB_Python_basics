"""
2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.
"""

while True:
    time_in_seconds = input('Введите количество секунд: ')
    if time_in_seconds.isdigit():
        time_in_seconds = int(time_in_seconds)
        hours = time_in_seconds // 3600
        minutes = time_in_seconds % 3600 // 60
        seconds = time_in_seconds % 3600 % 60
        print(f'В формате hh:mm:ss это будет {hours:02}:{minutes:02}:{seconds:02}')
        break
    else:
        print('К сожалению, вы ввели что-то другое.')
