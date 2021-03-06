# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.
seasons_dict = {'Зима': (1, 2, 12),
           'Весна': (3, 4, 5),
           'Лето': (6, 7, 8),
           'Осень': (9, 10, 11)} #создаем словарь
month_list = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь',
              'Октябрь', 'Ноябрь', 'Декабрь'] #создаем список
month = int(input('Введите номер месяца >>>'))
i = int(month - 1) #определяем номер индекса из списка месяцев

for key in seasons_dict.keys(): #Цикл поиска в словаре к какому сезону относится номер месяца
    if month in seasons_dict[key]:
        print(f" Сейчас время года >>> {key} \n А месяц >>> {month_list[i]}")
