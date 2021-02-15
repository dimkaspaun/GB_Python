# 1. Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

variables_list = [2, 3, 4, "Числа"]
variables_tuple = (8, 16, 32)
variables_set = {'abrakadabra'}
variables_dict = {"name": "Alex", 2: 400, "age": 18}
print(f"Тип списка >>> {type(variables_list)}")
print(f"Тип списка >>> {type(variables_tuple)}")
print(f"Тип списка >>> {type(variables_set)}")
print(f"Тип списка >>> {type(variables_dict)}")
