"""
Реализовать программу работы с органическими клетками.
Необходимо создать класс Клетка. В его конструкторе инициализировать параметр,
соответствующий количеству клеток (целое число).
В классе должны быть реализованы методы перегрузки арифметических операторов:
сложение (add()), вычитание (sub()), умножение (mul()), деление (truediv()).
Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение,
умножение и обычное (не целочисленное) деление клеток, соответственно.
В методе деления должно осуществляться округление значения до целого числа.
Сложение. Объединение двух клеток.
При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
Вычитание. Участвуют две клетки.
Операцию необходимо выполнять только если разность количества ячеек двух клеток больше нуля,
иначе выводить соответствующее сообщение.
Умножение. Создается общая клетка из двух.
Число ячеек общей клетки определяется как произведение количества ячеек этих двух клеток.
Деление. Создается общая клетка из двух.
Число ячеек общей клетки определяется как целочисленное деление количества ячеек этих двух клеток.
В классе необходимо реализовать метод make_order(),
принимающий экземпляр класса и количество ячеек в ряду.
Данный метод позволяет организовать ячейки по рядам.
Метод должен возвращать строку вида **\n\n***...,
где количество ячеек между \n равно переданному аргументу.
Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5.
Тогда метод make_order() вернет строку: **\n\n.
Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5.
Тогда метод make_order() вернет строку: **\n\n***.
"""
class Egg:

    def __init__(self, cells):
        self.cells = cells

    def __add__(self, other):
        return Egg(self.cells + other.cells)

    def __sub__(self, other):
        if self.cells <= other.cells:
            print('Вычитание невозможно, так как уходим в минус')
            raise ValueError
        return Egg(self.cells - other.cells)

    def __mul__(self, other):
        return Egg(self.cells * other.cells)

    def __truediv__(self, other):
        return Egg(round(self.cells / other.cells))

    def make_order(self, row):
        ordered = ['*' * row for _ in range(self.cells // row)]
        ordered.append('*' * (self.cells % row))
        return f'\n'.join(ordered)


if __name__ == '__main__':
    e1 = Egg(20)
    e2 = Egg(30)
    e3 = e1 + e2
    try:
        e4 = e3 - Egg(100)
    except ValueError as e:
        e4 = e3 - Egg(10)
    finally:
        print(f'e4.cells={e4.cells}')
    e5 = e3 * e4
    e6 = e5 / e1
    print(f'e1:7: cells({e1.cells})\n{e1.make_order(7)}')
    print(f'e2:7: cells({e2.cells})\n{e2.make_order(7)}')
    print(f'e3:7: cells({e3.cells})\n{e3.make_order(7)}')
    print(f'e4:7: cells({e4.cells})\n{e4.make_order(7)}')
    print(f'e5:70: cells({e5.cells})\n{e5.make_order(70)}')
    print(f'e6:7: cells({e6.cells})\n{e6.make_order(7)}')