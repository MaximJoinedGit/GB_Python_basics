"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
"""
import sys

input_parts = (sys.argv[1], sys.argv[2], sys.argv[3])


def full_salary(hours, salary, bonus):
    """
    Function calculate full salary for the month.
    :param hours: hours you worked
    :param salary: money per hour
    :param bonus: extra money per month
    :return: all the money you earned this month.
    """
    all_param = {
        'Отработанные часы': hours,
        'Заработная плата в час': salary,
        'Месячная премия': bonus
    }
    try:
        all_param_lst = list(map(int, all_param.values()))
        return (all_param_lst[0] * all_param_lst[1]) + all_param_lst[2]
    except ValueError:
        print('В строке было не число, повторите команду.')


money = full_salary(*input_parts)
if money:
    print(money)
