# 1. Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.
variables_int = 152
variables_float = 3.14
variables_str = "Строка"
variables_list = [2, 3, 4, "Числа"]
variables_tuple = (8, 16, 32)
variables_set = {'abrakadabra'}
variables_dict = {"name": "Alex", 2: 400, "age": 18} #создаем случайные пременные

mass_list = [variables_int, variables_float, variables_str, variables_list,
             variables_tuple, variables_set, variables_dict] #создаем переменную со списком
                                                             # переменных которые будем определять
for type_1 in mass_list:
    print(f'{type_1} >>> {type(type_1)}')   # цикл который выдаёт
                                            # значение переменной и тип переменной
