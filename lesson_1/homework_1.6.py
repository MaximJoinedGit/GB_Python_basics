"""
6. Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров.
Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего. Требуется определить номер дня,
на который общий результат спортсмена составить не менее b километров. Программа должна принимать значения параметров
a и b и выводить одно натуральное число — номер дня.
"""

a = input('Какой результат у спортсмена в первый день? ')
b = input('Какого результата он должен достичь? ')
i = 1
if a.isdigit() and b.isdigit():
    a, b = int(a), int(b)
    while a < b:
        a *= 1.1
        i += 1
    print(f'Если спортсмен будет прибавлять каждый день по 10%, то он достигнет результата на {i}-й день')