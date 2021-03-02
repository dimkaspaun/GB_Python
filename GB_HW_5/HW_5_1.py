"""
Создать программно файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""

import os

user_dir = 'user_dir'
file_path = os.path.join(user_dir, 'file_5_1.txt')
file = open(file_path, 'a', encoding='utf-8')

while True:
    string = input('Введите текст >>> ')

    if not string:
        file.close()
        print('Выход')
        break

    file.write(f'{string}\n')
