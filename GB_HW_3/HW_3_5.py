'''
5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
При нажатии Enter должна выводиться сумма чисел.
Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы завершается.
Если специальный символ введен после нескольких чисел, то вначале нужно добавить
сумму этих чисел к полученной ранее сумме и после этого завершить программу.
'''


def sum_list(*nums):
    sum = 0
    symbol = False
    for num in nums:
        try:
            if num:
                sum += float(num)
        except ValueError:
            symbol = True
    return sum, symbol


sigma = 0

while True:
    numbers_string = input("Введите числа через пробел (для выхода введите любой символ) >>>").split(' ')
    sum, stop_symbol = sum_list(*numbers_string)
    sigma += sum
    print(f'Сумма >>> {sigma}')

    if stop_symbol:
        break