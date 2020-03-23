"""
2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
Использовать формулу: длинаширинамасса асфальта для покрытия одного кв метра дороги асфальтом,
толщиной в 1 см*число см толщины полотна. Проверить работу метода.
Например: 20м*5000м*25кг*5см = 12500 т
"""


class Road:
    weight = 25
    height = 5

    def __init__(self, length: float, width: float):
        self.__length = length
        self.__width = width

    def mass(self):
        total_weight = self.__length * self.__width * self.weight * self.height

        return total_weight / 1000


road_part = Road(20, 5000)
print(f'Required mass - {road_part.mass()} tons')
