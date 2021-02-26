'''
2. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.

Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].
'''

import random
#генерируем список из 14 элементов с рандомными числами из промежутка от 1 до 999
list_start = [random.randint(1, 999) for _ in range(14)]
print("Стартовый список: ")
print(list_start)

def max_list(input_list: list):
    output_list = []
    for key, value in enumerate(input_list):
        if key+1 < len(input_list) and value < input_list[key+1]:
            output_list.append(input_list[key+1])

    return output_list

print('Результат по списку:')

print(max_list(list_start))