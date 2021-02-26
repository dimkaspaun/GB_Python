'''
1. Реализовать скрипт, в котором должна быть предусмотрена функция
расчета заработной платы сотрудника. В расчете необходимо
использовать формулу: (выработка в часах*ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо
запускать скрипт с параметрами.
'''
import sys

print('Входные параметры', sys.argv)
try:
    rate = int(sys.argv[1])
    hours = int(sys.argv[2])
    prize = int(sys.argv[3])
except ValueError:
    print("Invalid args")
    exit()

def salary(rate, hours, prize):
    return rate * hours + prize


print(f'Расчет заработной платы сотрудника >>> {salary(rate, hours, prize)} руб.')