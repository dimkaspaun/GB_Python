# Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два элемента —
# номер товара и словарь с параметрами
# (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
# Пример готовой структуры:
# [
#     (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
#     (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
#     (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
# ]
# Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара,
# например название, а значение — список значений-характеристик, например список названий товаров.
# Пример:
# {
#     “название”: [“компьютер”, “принтер”, “сканер”],
#     “цена”: [20000, 6000, 2000],
#     “количество”: [5, 2, 7],
#     “ед”: [“шт.”]
# }
products_list = []
i = 1
while True:  # вечный цикл

    products_list.append(  # Добавить элемент в конец списка products_list
        (i, dict({'название': str(input('Введите название товара >>> ')),  # порядковый номер совподает с номером цикла
                  'цена': float(input('Введите цену товара >>> ')),  # округляем до целого числа
                  'количество': int(input('Введите кол-во товара >>> ')),
                  'eд': str(input('Введите ед. товара >>> ')),
                  }))
    )
    if int(input(
            "Добавить следующий товар? Введите цифру 1 или 2 ((1да)/(2нет)) >>> ")) == 2:  # условие при котором цикл завершится
        break
    i += 1
print(f'Список товаров:{products_list}')

output_dict = dict({})
for product in products_list:  # Цикл наполнения output_dict
    for key, value in product[-1].items():  # Цикл проверки ключа и значения
        if key in output_dict:  # Проверка есть ли ключи в словаре output_dict
            if value not in output_dict.get(key):  # Если такое значение уже есть в списке ключа то не добавлять
                output_dict.get(key).append(value)  # Если такого значение нет то добавить его в список ключа
        else:
            output_dict.update({key: [value]})  # Создает ключи в output_dict с вложиным списком

print(f'Собрана аналитика: {output_dict}')
