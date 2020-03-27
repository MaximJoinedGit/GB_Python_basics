"""
3. Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка.
В его конструкторе инициализировать параметр, соответствующий количеству клеток (целое число).
В классе должны быть реализованы методы перегрузки арифметических операторов:
сложение (add()), вычитание (sub()), умножение (mul()), деление (truediv()).
Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение и
обычное (не целочисленное) деление клеток, соответственно.
В методе деления должно осуществляться округление значения до целого числа.

Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.

Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек двух клеток больше
нуля, иначе выводить соответствующее сообщение.

Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение количества ячеек этих
двух клеток.

Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление количества
ячеек этих двух клеток.

В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду.
Данный метод позволяет организовать ячейки по рядам.
Метод должен возвращать строку вида **\n\n***..., где количество ячеек между \n равно переданному аргументу.
Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5.
Тогда метод make_order() вернет строку: **\n\n.
Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5.
Тогда метод make_order() вернет строку: **\n\n***.
"""

from math import floor


class Cell:
    """
    Class Cell is working with organic cells (add, sub, mul and div).
    """
    def __init__(self, number: int):
        self.number = number

    def __str__(self):
        return str(self.number)

    def __add__(self, other):
        """
        Adding nucleuses.
        :param other: Another cell.
        :return: int.
        """
        self.add_cell = self.number + other.number
        return Cell(self.add_cell)

    def __sub__(self, other):
        """
        Substract nucleuses. If difference is lower than zero returns message.
        :param other: Another cell.
        :return: int or text message.
        """
        if self.number > other.number:
            self.sub_cell = self.number - other.number
            return Cell(self.sub_cell)
        else:
            return f'{self.number} < {other.number}\nDifference is lower than zero!'

    def __mul__(self, other):
        """
        Multiply nucleuses.
        :param other: Another cell.
        :return: int.
        """
        self.mul_cell = self.number * other.number
        return Cell(self.mul_cell)

    def __truediv__(self, other):
        """
        Divide nucleuses. Includes exception ZeroDivisionError. Transfoms float to int by method floor.
        :param other: Another cell.
        :return: int.
        """
        try:
            self.div_cell = self.number / other.number
            return Cell(floor(self.div_cell))
        except ZeroDivisionError:
            return f'Division by zero!'

    def make_order(self, in_row: int):
        """
        Shows in scheme how many rows will have all the nucleuses if in the row are defined number of ones.
        :param in_row: nucleuses in the row.
        :return: str.
        """
        dot = '*'
        for row in range(self.number // in_row):
            print(f'{dot * in_row}')
        print(f'{dot * (self.number % in_row)}')


if __name__ == '__main__':
    first = Cell(50)
    second = Cell(25)
    third = Cell(0)
    print(first + second)
    print(first - second)
    print(first * second)
    print(first / second)
    print(second - first)
    print(first / third)
    dots_in_row = first - second
    dots_in_row.make_order(10)
