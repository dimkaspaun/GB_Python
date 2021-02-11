number = int(input("Введите целое число>>> "))
max_numbers = number % 10
number = number // 10
while number > 0:
    if number % 10 > max_numbers:
        max_numbers = number % 10
    number = number // 10

print('Cамая большая цифра в числе: ', max_numbers)
