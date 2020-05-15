"""
3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список.
Класс-исключение должен контролировать типы данных элементов списка.
Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока пользователь сам не остановит
работу скрипта, введя, например, команду “stop”. При этом скрипт завершается, сформированный список выводится на экран.
Подсказка: для данного задания примем, что пользователь может вводить только числа и строки.
При вводе пользователем очередного элемента необходимо реализовать проверку типа элемента и вносить его в список,
только если введено число. Класс-исключение должен не позволить пользователю ввести текст (не число) и отобразить
соответствующее сообщение. При этом работа скрипта не должна завершаться.
"""


class Value(Exception):
    """
    Class to make exception for nondigit input.
    """
    def __init__(self, text):
        self.text = text


lst = []
while True:
    user_input = input('Enter number to add in list or \'q\' to exit: ')
    if user_input == 'q':
        break
    try:
        # Checks is the element integer.
        if user_input.isdigit():
            lst.append(int(user_input))
        # Checks is the element float.
        elif not user_input.isdigit() and \
                (len(user_input.split('.')) < 3
                 and user_input.split('.')[0].isdigit()
                 and user_input.split('.')[1].isdigit()):
            lst.append(float(user_input))
        else:
            raise Value('It\'s not a number. This value will be ignored!')
    except Value as v:
        print(v)
print(' '.join(map(str, lst)))
