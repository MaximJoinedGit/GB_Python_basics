"""
4. Реализуйте базовый класс Car.
У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""

from random import randint, choice


class Car:
    def __init__(self, name: str, is_police: bool):
        self.name = name
        self.is_police = is_police
        self.speed = randint(20, 80)
        self.color = choice(['Red', 'Green', 'Blue', 'Yellow', 'Black', 'White', 'Purple'])
        self.direction = choice(['left', 'right'])

    def go(self):
        print('The car started driving.')

    def stop(self):
        print('The car stopped')

    def turn(self):
        print(f'The car turned to the {self.direction}')

    def show_speed(self):
        print(f'Your current speed {self.speed}')


class TownCar(Car):
    def __init__(self, name):
        super().__init__(name, is_police=False)

    def show_speed(self):
        print(f'Speed limit! Current speed {self.speed}') if self.speed > 60 else print(f'Current speed {self.speed}')


class SportCar(Car):
    def __init__(self, name):
        super().__init__(name, is_police=False)


class WorkCar(Car):
    def __init__(self, name):
        super().__init__(name, is_police=False)

    def show_speed(self):
        print(f'Speed limit! Current speed {self.speed}') if self.speed > 40 else print(f'Current speed {self.speed}')


class PoliceCar(Car):
    def __init__(self, name):
        super().__init__(name, is_police=True)


town = TownCar('Lada')
sport = SportCar('Ferrari')
work = WorkCar('GAZ')
police = PoliceCar('Ford')

town.go()
print(f'The car is {town.color} {town.name}')
town.show_speed()
town.turn()
town.stop()
print(f'{25*"-"}')

sport.go()
print(f'The car is {sport.color} {sport.name}')
sport.show_speed()
sport.turn()
sport.stop()
print(f'{25*"-"}')


work.go()
print(f'The car is {work.color} {work.name}')
work.show_speed()
work.turn()
work.stop()
print(f'{25*"-"}')


police.go()
print(f'The car is {police.color} {police.name}')
police.show_speed()
police.turn()
police.stop()
print(f'{25*"-"}')
