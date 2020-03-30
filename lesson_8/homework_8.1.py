"""
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и
преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
"""

check_month = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}


class DateValid(Exception):
    """
    Exception class to make my own exception.
    """
    def __init__(self, text):
        self.txt = text


class Date:
    """
    Class Date with two methods. One for transform str to int and the second to check is date valid or not.
    """
    def __init__(self, date_input: str):
        """
        Class accepts date in format "dd-mm-yyyy".
        :param date_input: str
        """
        self.date_input = date_input

    @classmethod
    def deformation(cls, date_input):
        """
        Transforms date to three integer numbers.
        :param date_input: str
        :return: day: int, month: int, year: int
        """
        day, month, year = map(int, date_input.split('-'))
        return day, month, year

    @staticmethod
    def validation(day, month, year):
        """
        Method shows is entered date valid or not.
        :param day: int
        :param month: int
        :param year: int
        """
        try:
            # Checks is the year leap or not. If year is leap we change number of days in February to 29.
            if not year % 4 and (not (year % 100) or year % 400):
                check_month[2] = 29
            # Date validation.
            if not 1900 < year < 2078 or not 0 < month < 13 or not 0 < day < check_month[month] + 1:
                raise DateValid('You entered invalid date.')
        except DateValid as y_valid:
            print(y_valid)
        else:
            print(f'You entered date {day:02}.{month:02}.{year}')


if __name__ == '__main__':
    d, m, y = Date.deformation('10-11-2005')
    Date.validation(d, m, y)
