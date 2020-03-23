"""
5. Реализовать класс Stationery (канцелярская принадлежность).
Определить в нем атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.”
Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер). В каждом из классов реализовать
переопределение метода draw. Для каждого из классов методы должен выводить уникальное сообщение. Создать экземпляры
классов и проверить, что выведет описанный метод для каждого экземпляра.
"""


class Stationery:
    def __init__(self, thing: str):
        self.thing = thing

    def draw(self):
        print('Запуск отрисовки.')


class Pen(Stationery):
    def __init__(self):
        super().__init__(thing='Ручка')

    def draw(self):
        print(f'Запуск отрисовки с помощью инструмента {self.thing}')


class Pencil(Stationery):
    def __init__(self):
        super().__init__(thing='Карандаш')

    def draw(self):
        print(f'Запуск отрисовки с помощью инструмента {self.thing}')


class Handle(Stationery):
    def __init__(self):
        super().__init__(thing='Маркер')

    def draw(self):
        print(f'Запуск отрисовки с помощью инструмента {self.thing}')


first = Stationery('Любой предмет.')
second = Pen()
third = Pencil()
fourth = Handle()
first.draw()
second.draw()
third.draw()
fourth.draw()
