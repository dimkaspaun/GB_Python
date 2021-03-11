"""
Создайте собственный класс-исключение, который должен проверять содержимое списка на
отсутствие элементов типа строка и булево. Проверить работу исключения на реальном
примере. Необходимо запрашивать у пользователя данные и заполнять список.
Класс-исключение должен контролировать типы данных элементов списка.
"""


class Exception_Error(Exception):

    def check_str(self, my_list):
        try:
            for el in my_list:
                if type(el) == str:
                    raise Exception_Error("Строка содержит элемент типа данных str: ")

        except Exception_Error as err:
            print(err, el)

    def check_bool(self, my_list):
        try:
            for el in my_list:
                if type(el) == bool:
                    raise Exception_Error("Строка содержит элемент типа данных bool: ")
        except Exception_Error as err:
            print(err, el)


input_list = [10, 2, 'строка', bool(50)]
print("Введенный список: ", input_list, "\n")
my_err = Exception_Error()
my_err.check_str(input_list)
my_err.check_bool(input_list)
