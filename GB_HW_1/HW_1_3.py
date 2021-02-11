# 3. Узнайте у пользователя число n.
# Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3.
# Считаем 3 + 33 + 333 = 369.
user_numbers = int(input("Введите положительное число>>>"))
result_2 = int(f"{user_numbers}{user_numbers}")
result_3 = int(f"{user_numbers}{user_numbers}{user_numbers}")
result = int(user_numbers + result_2 + result_3)
print(f"Результат сложения: {user_numbers}+{result_2}+{result_3} = {result}")
