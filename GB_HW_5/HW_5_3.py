"""
Создать текстовый файл (не программно), построчно записать фамилии
сотрудников и величину их окладов (не менее 10 строк).
Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
Пример файла:
Иванов 23543.12
Петров 13749.32
"""

import os

user_dir = 'user_dir'
file_path = os.path.join(user_dir, 'file_5_3.txt')
file = open(file_path, 'r', encoding='utf-8')
lines = file.readlines()

sum = 0
for row in lines:
    line = row.split()

    if (float(line[1]) < 20000):
        print(f'{line[0], line[1]} Оклад сотрудника менее 20 тыс.руб.')

    sum += float(line[1]) / len(lines)

print(f'Средняя величина дохода сотрудников {round(sum, 2)} руб')

file.close()
