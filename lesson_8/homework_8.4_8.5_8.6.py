"""
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в
определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, а также других
данных, можно использовать любую подходящую структуру, например словарь.

6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
изученных на уроках по ООП.
"""


class Failure(Exception):
    """
    Class exception.
    """
    def __init__(self, text):
        self.text = text


class Warehouse:
    """
    Warehouse with total capacity and capacity by kind of goods.
    """
    _capacity = {'total': 100, 'printer': 0, 'scanner': 0, 'xerox': 0}

    def __init__(self):
        self._free_space = Warehouse._capacity['total']

    @staticmethod
    def transfer(from_to: str, direction: str, number: int, thing: str):
        """
        Method performs transfer from and to warehouse.
        :param from_to: takes 'from' or 'to'. str
        :param direction: takes name of department of sender or receiver. str
        :param number: how many good we need to transfer. int
        :param thing: what we should transfer. str
        """
        if from_to == 'from':
            try:
                if Warehouse._capacity['total'] < number:
                    raise Failure(f'We need more free space. '
                                  f'We can\'t place {number - Warehouse._capacity["total"]} {thing}')
                else:
                    Warehouse._capacity[thing] += number
                    print(f'We transfered {number} {thing} from {direction}. '
                          f'Now we have {Warehouse._capacity[thing]} {thing}')
            except Failure as f:
                print(f)
        elif from_to == 'to':
            try:
                if Warehouse._capacity[thing] < number:
                    raise Failure(f'We don\'t have {number} {thing} on warehouse!')
                else:
                    Warehouse._capacity[thing] -= number
                    print(f'We transfered {number} {thing} to {direction}. '
                          f'Now we have {Warehouse._capacity[thing]} {thing}')
            except Failure as f:
                print(f)


class OfficeEquipment(Warehouse):
    """
    Parent-class for all equipment.
    """
    def __init__(self, price: float, firm: str, quantity: int, color: str):
        """
        Defines input parameters. Also calculates could we accept goods to warehouse or not.
        :param price: price of good. float
        :param firm: firm of good. str
        :param quantity: how many goods. int
        :param color: color of good. str
        """
        super().__init__()
        self.price = price
        self.firm = firm
        self.quantity = quantity
        self.color = color
        try:
            Warehouse._capacity['total'] -= self.quantity
            if Warehouse._capacity['total'] < 0:
                raise Failure(f'Run out of free space. Available {Warehouse._capacity["total"] + self.quantity}')
        except Failure as f:
            print(f)


class Printer(OfficeEquipment):
    """
    Child-class for equipment kind "printer".
    """
    def __init__(self, price, firm, quantity, color, print_kind: str, print_color: str, print_speed: float):
        """
        Defines printer's parameters. Price, firm, quantity and color it takes from Parent-class OfficeEquipment.
        :param print_kind: inkjet, laserjet etc. str
        :param print_color: color or black-white. str
        :param print_speed: speed or printing (sheets per minute). float
        """
        super().__init__(price, firm, quantity, color)
        self.kind = print_kind
        self.color = print_color
        self.print_speed = print_speed
        Warehouse._capacity['printer'] += quantity

    @property
    def total_printer(self):
        """
        Shows how many printers we have on warehouse.
        :return: f-string
        """
        return f'Now we have {Warehouse._capacity["printer"]} printers.'


class Scanner(OfficeEquipment):
    """
    Child-class for equipment kind "scanner".
    """
    def __init__(self, price, firm, quantity, color, scan_kind: str, scan_speed: float):
        """
        Defines scanner's parameters. Price, firm, quantity and color it takes from Parent-class OfficeEquipment.
        :param scan_kind: color or black-white. str
        :param scan_speed: speed or scanning (sheets per minute). float
        """
        super().__init__(price, firm, quantity, color)
        self.scan_kind = scan_kind
        self.scan_speed = scan_speed
        Warehouse._capacity['scanner'] += quantity

    @property
    def total_scanner(self):
        """
        Shows how many scanners we have on warehouse.
        :return: f-string
        """
        return f'Now we have {Warehouse._capacity["scanner"]} scanners.'


class Xerox(OfficeEquipment):
    """
    Child-class for equipment kind "scanner".
    """
    def __init__(self, price, firm, quantity, color, xer_kind: str, xer_speed: float):
        """
        Defines xerox's parameters. Price, firm, quantity and color it takes from Parent-class OfficeEquipment.
        :param xer_kind: color or black-white. str
        :param xer_speed: speed or copying (sheets per minute). float
        """
        super().__init__(price, firm, quantity, color)
        self.xer_kind = xer_kind
        self.xer_speed = xer_speed
        Warehouse._capacity['xerox'] += quantity

    @property
    def total_xerox(self):
        """
        Shows how many xeroxes we have on warehouse.
        :return: f-string
        """
        return f'Now we have {Warehouse._capacity["xerox"]} xeroxes.'


if __name__ == '__main__':
    a = Printer(100, 'HP', 15, 'black', 'laser', 'color', 40)
    b = Scanner(80, 'Samsung', 20, 'grey', 'black-n-white', 20)
    c = Xerox(120, 'Xerox', 10, 'white', 'color', 10)
    d = Printer(110, 'Canon', 25, 'white', 'laser', 'color', 60)

    print(1)
