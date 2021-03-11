"""
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля в
качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с
ошибкой.
"""

class MyException(Exception):

    def division_func(self, a, b):
        try:
            res = round(a / b, 2)
        except ZeroDivisionError:
            print(f"{a} / {b}  Деление на ноль разбирают в разделе высшей математики вместе с бесконечными величинами\n")
        else:
            print(f"{a} / {b} = {res} \n")


m_e = MyException()

m_e.division_func(10, 3)
m_e.division_func(20, 0)
m_e.division_func(9, 3)
m_e.division_func(0, 20)
