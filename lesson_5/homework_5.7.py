"""
7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.
"""

import json

companies = {}
average = 0
count = 0
with open('homework_5.7.txt', 'r', encoding='utf-8') as r:
    for company in r:
        stat_company = company.split()
        try:
            companies[stat_company[0]] = int(stat_company[2]) - int(stat_company[3])
        except ValueError:
            print('Где-то в файле значение выручки задано не числом. Проверьте файл и перезапустите программу.')
for profit in companies.values():
    if profit > 0:
        count += 1
        average += profit
average_profit = {'Average_profit': round(average / count)}
full_data = [companies, average_profit]
with open('homework_5.7.json', 'w', encoding='utf-8') as w:
    json.dump(full_data, w)
