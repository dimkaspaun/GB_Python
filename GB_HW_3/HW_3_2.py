'''
2. Реализовать функцию, принимающую несколько параметров, описывающих данные
пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
'''


def userdata(name, lastname, birthyear, city, email, tel):
    print(f"Фамилия: {lastname} Имя: {name}  Год рождения: {birthyear} Город: {city} email: {email} Телефон: {tel}")


userdata(lastname="Петров", name="Пётр",  birthyear=1980, city="Москва", email="1@.ru", tel=789456)
userdata(lastname="Иванов", name="Иван",  birthyear=1970, city="Тюмень", email="2@.ru", tel=123456)
