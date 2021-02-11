second_user = int(input("Введите время в секундах >>>"))
hour = int(second_user // 3600)
minutes = int(second_user // 60) % 60
second = int(second_user % 60)

print(f"{hour} ч. {minutes} м.  {second} с.")
