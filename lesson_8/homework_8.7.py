"""
7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку
методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса (комплексные числа)
и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.
"""


class Complex:
    """
    Class of complex numbers.
    """
    def __init__(self, real: float, imaginary: float):
        """
        We accept two parts: real and imaginary.
        :param real: float
        :param imaginary: float
        """
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        """
        Calculates sum of two complex numbers.
        :param other: another complex number.
        :return: complex num.
        """
        self.sum_complex_num = Complex((self.real + other.real), (self.imaginary + other.imaginary))
        return self.sum_complex_num

    def __mul__(self, other):
        """
        Calculates multiplying of two complex numbers.
        :param other: another complex number.
        :return: complex num.
        """
        self.mul_complex_num = Complex((self.real * other.real - self.imaginary * other.imaginary),
                                (self.real * other.imaginary + self.imaginary * other.real))
        return self.mul_complex_num

    def __str__(self):
        """
        Shows number as complex number.
        :return: f-string
        """
        return f'{self.real:02} + {self.imaginary:02}i'


if __name__ == '__main__':
    a = Complex(10.2, 20)
    b = Complex(1, 2)
    c = a + b
    d = a * b
    print(c)
    print(d)
