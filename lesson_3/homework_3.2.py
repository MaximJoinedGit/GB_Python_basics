"""
2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения,
город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
"""


def user_input(inf):
    """
    Function accepts defined dictionary and helps to user to enter the information about himself.
    :param inf: values in dictionary are tuples (explanation to user, expected type).
    :type inf: dict
    :return: another dictionary with information about human.
    """
    human = {}
    for info, data in inf.items():
        while True:
            user = input(f'{data[0]}: ')
            try:
                user = data[1](user)
                break
            except ValueError:
                print(f'Вы ввели не {data[0]}! Повторите ввод.')
        human[info] = user
    return human


def print_data(**kwargs):
    """
    Function only accept dictionary with data about user and shows the info.
    :param kwargs: dictionary, keys are kind of information and values is the information.
    :type kwargs: dict
    :return: prints the info with using template.
    """
    return f'Имя: {kwargs.get("name")}, Фамилия: {kwargs.get("surname")}, Год рождения: {kwargs.get("birth_year")},' \
           f' Город проживания: {kwargs.get("city")}, Адрес эл. почты: {kwargs.get("email")},' \
           f' Номер телефона: {kwargs.get("phone")}.'


person = {
    'name': ('Имя', str),
    'surname': ('Фамилия', str),
    'birth_year': ('Год рождения', int),
    'city': ('Город', str),
    'email': ('Эл. почта', str),
    'phone': ('Телефон', int),
}

our_person = user_input(person)
print(print_data(**our_person))
