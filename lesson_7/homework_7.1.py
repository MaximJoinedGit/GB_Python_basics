"""
1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод init()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода add() для реализации операции сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с
первым элементом первой строки второй матрицы и т.д.
"""


class Matrix:
    def __init__(self, matr: list):
        self.matr = matr

    def __str__(self):
        """
        Redefines method to show matrix.
        :return: Matrix as we used to see.
        """
        return '\n'.join(map(str, (' '.join(map(str, elem)) for elem in self.matr)))

    def __add__(self, other):
        """
        Makes possible to sum matrix and matrix.
        :param other: Second matrix.
        :return: New matrix of class Matrix.
        """
        self.new_matr = [[0 for _ in range(len(self.matr[row]))] for row in range(len(self.matr))]
        for each in range(len(self.matr)):
            for elem in range(len(self.matr[each])):
                self.new_matr[each][elem] = self.matr[each][elem] + other.matr[each][elem]
        return Matrix(self.new_matr)


if __name__ == '__main__':
    first = Matrix([[0, 1, 2, 3], [3, 2, 1, 0], [5, 6, 7, 8]])
    second = Matrix([[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]])
    both = first + second
    print(first, second, both, sep='\n\n')
