revenue = int(input("Введите сумму выручки >>>"))
costs = int(input("Введите сумму издержек >>>"))
if revenue > costs:
    print("Поздравляем вас, у вас был прибыльный период")
    staff = int(input("Введите количество сотрудников >>>"))
    staff_revenue = round((revenue - costs) / staff, 2)
    print(f"Прибыль на одного сотрудника составляет >>> {staff_revenue} руб.")
else:
    print("Извините но вы работаете в убыток")
