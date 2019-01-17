# Задача-1:
# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример: Дано: [2, -5, 8, 9, -25, 25, 4]   Результат: [3, 5, 2]

import math
import random
print("#1")
data1 = []
data2 = []
filler = "empty"
while filler != "end":
    filler = input("Input next element or ""end"": ")
    if filler == "end":
        print(data1)
        break
    else:
        data1.append(int(filler))
filler = "empty"
for i in range(0, data1.__len__()):
    if (data1[i] >= 0) and (math.sqrt(data1[i]).is_integer()):
        data2.append(math.sqrt(data1[i]))
print(data2)

# Задача-2: Дана дата в формате dd.mm.yyyy, например: 02.11.2013.
# Ваша задача вывести дату в текстовом виде, например: второе ноября 2013 года.
# Склонением пренебречь (2000 года, 2010 года)

print("#2")
day = ["Первое", "Второе", "Третье", "Четвертное", "Пятое", "Шестое", "Седьмое", "Восьмое", "Девятое", "Десятое",
       "Одиннадцатое", "Двенадцатое", "Тринадцатое", "Четырнадцатое", "Пятнадцатое", "Шестнадцатое",
       "Семнадцатое", "Восемнадцатое", "Девятнадцатое", "Двадцатое", "Двадцать первое", "Двадцать второе",
       "Двадцать третье", "Двадцать четвертое", "Двадцать пятое", "Двадцать шестое", "Двадцать седьмое",
       "Двадцать восьмое", "Двадцать девятое", "Тридцатое", "Тридцать первое"]
month = ["января", "февраля", "марта", "апреля", "мая", "июня", "июля", "августа", "сентября", "октября", "ноября",
         "декабря"]
data3 = input("Input date in dd.mm.yyyy format: ")
numeric_day = int(data3[:2])
numeric_month = int(data3[3:5])
if 0 < numeric_day <= 31 and 0 < numeric_month <= 12 or (numeric_day < 29 and numeric_month == 2):
    string_date = "{} {} {} года".format(day[numeric_day-1], month[numeric_month-1], data3[6:])
    print(string_date)
else:
    print("Введите корректную дату")
# print(data3, numeric_day, numeric_month)


# Задача-3: Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random

print("#3")
list_length = int(input("input length: "))
the_list = []
i = 0
for i in range(0, list_length):
    the_list.append(random.randint(-100, 100))
print(the_list)


# Задача-4: Дан список, заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут: 
# а) неповторяющиеся элементы исходного списка:
# например, lst = [1, 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 2, 4, 5, 6]
# б) элементы исходного списка, которые не имеют повторений:
# например, lst = [1 , 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 4, 6]

print("#4")
lst = []
filler = "empty"
while filler != "end":
    filler = input("Input next element or ""end"": ")
    if filler == "end":
        print(lst)
        break
    else:
        lst.append(int(filler))
filler = "empty"
set_lst = set(lst)
lst_set_lst = list(set_lst)
print(lst_set_lst)
for i in range(0, lst_set_lst.__len__()):
    if lst.count(lst_set_lst[i]) > 1:
        while lst.count(lst_set_lst[i]) != 0:
            lst.remove(lst_set_lst[i])
print(lst)
