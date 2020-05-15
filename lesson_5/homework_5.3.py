"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
"""

salaries = {}
min_rich = 20000
average = 0
with open('homework_5.3.txt', 'r', encoding='utf-8') as m:
    for human in m:
        salaries[human.split()[0]] = human.split()[1]
for person, money in salaries.items():
    try:
        print(f'{person} получает меньше 20000 рублей.') if int(salaries[person]) < min_rich else None
        average += int(salaries[person])
    except ValueError:
        print('В исходном файле ошибка.')
print(f'Средняя заработная плата в компании {round(average / len(salaries))}')
