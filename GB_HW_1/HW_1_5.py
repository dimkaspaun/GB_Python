# 5. Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма
# (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
# Выведите соответствующее сообщение. Если фирма отработала с прибылью,
# вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль
# фирмы в расчете на одного сотрудника.
revenue = int(input("Введите сумму выручки >>>"))
costs = int(input("Введите сумму издержек >>>"))
if revenue > costs: #если выручка больше издержек то тогда можно
                    # будет запросить количество сотрудников если меньше то смысла
                    # нет и выдаем соотвествующее сообщение
    print("Поздравляем вас, у вас был прибыльный период")
    staff = int(input("Введите количество сотрудников >>>"))
    staff_revenue = round((revenue - costs) / staff, 2) #разницу между приболью и издержкой
                                                        # делим на количество сотрудников,
                                                        # огроничили количество знаков после
                                                        # запятой до двух round (__,2)
    print(f"Прибыль на одного сотрудника составляет >>> {staff_revenue} руб.")
else:
    print("Извините но вы работаете в убыток")
