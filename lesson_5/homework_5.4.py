"""
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""

rus_nums = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре'
}
r = open('homework_5.4.txt', 'r', encoding='utf-8')
w = open('homework_5.4.new.txt', 'w', encoding='utf-8')
for line in r:
    temp_line = line.split()
    temp_line[0] = rus_nums[line.split()[0]]
    w.write(' '.join(temp_line) + '\n')
r.close()
w.close()
