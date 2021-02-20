''' 1. Реализовать функцию, принимающую два числа (позиционные аргументы)
и выполняющую их деление. Числа запрашивать у пользователя,
предусмотреть обработку ситуации деления на ноль. '''


def division(var1, var2):
    try:
        return var1 / var2
    except ZeroDivisionError:

        print('На ноль делить нельзя!')
        return None


result = division(int(input("Введите делимое число >>>")), int(input("Введите делитель>>>")))

try:
    result = round(result, 2)
except TypeError:
    print()
else:
    print(f"Результат деления = {result}")
