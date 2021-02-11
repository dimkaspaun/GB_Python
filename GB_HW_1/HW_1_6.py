km_a = int(input("Введите стартовый результат >>> "))
km_b = int(input("Введите конечную цель >>> "))
count = 1
while km_a < km_b:
    km_a = round(km_a * 1.1, 2)
    count += 1
    print(f"День >>> {count}  Растояние {km_a}")
print(f"Потребуется вот такое количество дней >>> {count} и результат будет вот такой >>> {km_a}")
