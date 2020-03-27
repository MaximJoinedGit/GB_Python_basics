"""
2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры: размер (для пальто)
и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
"""

from abc import ABC, abstractmethod


class Clothes(ABC):
    """
    Abstract class Clothes.
    """
    total = 0

    def __init__(self, name: str):
        self.name = name
        self.total = Clothes.total

    @abstractmethod
    def calc_fabric(self):
        """
        Abstract method calc_fabric.
        """
        pass


class Coat(Clothes):
    """
    Class coat is for every coat unit.
    """

    def __init__(self, name, v: int):
        super().__init__(name)
        self.v = v
        self.fabric_coat = self.v / 6.5 + 0.5
        Clothes.total += self.fabric_coat

    @property
    def calc_fabric(self):
        """
        Method for total fabric needed to make all units.
        :return: f-string
        """
        return f'We need {self.fabric_coat:.02} fabric for the Coat.'

    @calc_fabric.setter
    def calc_fabric(self, value):
        """
        Setter. Needed to change value size in unit and calc new total fabric.
        :param value: new value for size coat.
        :return: float
        """
        Clothes.total -= self.fabric_coat
        self.v = value
        self.fabric_coat = self.v / 6.5 + 0.5
        Clothes.total += self.fabric_coat
        print(f"""We changed parameter to {value}""")


class Suit(Clothes):
    """
    Class suit is for every suit unit.
    """

    def __init__(self, name, h: int):
        super().__init__(name)
        self.h = h
        self.fabric_suit = 2 * self.h + 0.3
        Clothes.total += self.fabric_suit

    @property
    def calc_fabric(self):
        """
        Method for total fabric needed to make all units.
        :return: f-string
        """
        return f'We need {self.fabric_suit} fabric for the Suit.'

    @calc_fabric.setter
    def calc_fabric(self, value):
        """
        Setter. Needed to change value height in unit and calc new total fabric.
        :param value: new value for height.
        :return: float
        """
        Clothes.total -= self.fabric_suit
        self.h = value
        self.fabric_suit = 2 * self.h + 0.3
        Clothes.total += self.fabric_suit
        print(f"""We changed parameter to {value}""")


if __name__ == '__main__':
    first_coat = Coat('My first coat', 10)
    second_coat = Coat('My second coat', 20)
    first_suit = Suit('My first suit', 10)
    second_suit = Suit('My first suit', 20)
    print(first_coat.calc_fabric, second_coat.calc_fabric, first_suit.calc_fabric, second_suit.calc_fabric,
          sep='\n', end='\n\n')

    print(first_coat.calc_fabric)
    print(f'Total fabric we need is {Clothes.total:.04}')
    first_coat.calc_fabric = 30
    print(first_coat.calc_fabric)
    print(f'Total fabric we need is {Clothes.total:.04}')

    print(first_suit.calc_fabric)
    print(f'Total fabric we need is {Clothes.total:.04}')
    first_suit.calc_fabric = 60
    print(first_suit.calc_fabric)
    print(f'Total fabric we need is {Clothes.total:.04}')
