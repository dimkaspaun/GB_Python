# 2. Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().
count_list = [] # создание пустого списка
quantity_n = int(input("Введите длину списка: "))
for i in range(0, quantity_n): #цикл по заполнению списка, где длина списка задается пользователем
    numbers = int(input(f"Введите число >>>"))
    count_list.append(numbers) #добавление значения в список

if len(count_list) % 2 == 0: # проверка на четность длины списка
    i = 0
    while i < len(count_list): # цикл обмена местами, весех элементов
        element = count_list[i]
        count_list[i] = count_list[i + 1]
        count_list[i + 1] = element
        i += 2
else:
    i = 0
    while i < len(count_list) - 1: #цикл обмена местами, кроме последнего элементов
        element = count_list[i]
        count_list[i] = count_list[i + 1]
        count_list[i + 1] = element
        i += 2
print(count_list)
