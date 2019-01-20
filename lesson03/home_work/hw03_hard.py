import os

# Задание-1:
# Написать программу, выполняющую операции (сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате:
# n x/y ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.
# Примеры:
# Ввод: 5/6 + 4/7 (всё выражение вводится целиком в виде строки)
# Вывод: 1 17/42  (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 1/3


# Задание-2:
# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки
# они получают удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"


# даем одну сырую строку, получаем обработанный список без лишних символов
def parse_raw_lines(one_line):
    one_line = one_line.split(" ")
    for i in reversed(range(one_line.__len__())):
        if one_line[i] == '':
            one_line.pop(i)
        one_line[i] = one_line[i].rstrip()
    return one_line


with open(os.path.join("data", "workers.txt"), encoding="utf-8") as workers:
    workers_content = workers.readlines()
with open(os.path.join("data", "hours_of"), encoding="utf-8") as hours:
    hours_content = hours.readlines()

# получаем массивы, которые будут использоватся для дальнейшего сопоставления сотрудник, норма часов / выработка
all_workers = []
all_worked_hours = []
for x in range(workers_content.__len__()):
    all_workers.append(parse_raw_lines(workers_content[x]))
for x in range(hours_content.__len__()):
    all_worked_hours.append(parse_raw_lines(hours_content[x]))


# сопоставляем сотрудника и его выработку с нормой
for x in range(all_workers.__len__()):
    for i in range(all_worked_hours.__len__()):
        if all_workers[x][0] == all_worked_hours[i][0] and all_workers[x][1] == all_worked_hours[i][1]:
            all_workers[x].append(all_worked_hours[i][2])

# удаляем лишний список с заголовками столбцов из нашего массива для дальнейших рассчетов
all_workers.pop(0)
# определяем что делать с ЗП по соотношению норма / выработка
zp = []
for i in range(all_workers.__len__()):
    one_hour_cost = int(all_workers[i][2]) / int(all_workers[i][4]) #float
    if int(all_workers[i][5]) < int(all_workers[i][4]):
        #name, surname, zp posle vicheta
        vichet = int(all_workers[i][2])-(int(all_workers[i][4])-int(all_workers[i][5]))*one_hour_cost
        zp.append([all_workers[i][0], all_workers[i][1], vichet])
    elif int(all_workers[i][5]) > int(all_workers[i][4]):
        pribavka = int(all_workers[i][2])+(int(all_workers[i][5])-int(all_workers[i][4]))*one_hour_cost*2
        zp.append([all_workers[i][0], all_workers[i][1], pribavka])
    else:
        zp.append([all_workers[i][0], all_workers[i][1], all_workers[i][2]])
# Вывод на экран в формате вложенных списков [Имя, Фамилия, ЗП]
print(zp)



# Задание-3:
# Дан файл ("data/fruits") со списком фруктов.
# Записать в новые файлы все фрукты, начинающиеся с определенной буквы.
# Т.е. в одном файле будут все фрукты на букву “А”, во втором на “Б” и т.д.
# Файлы назвать соответственно.
# Пример имен файлов: fruits_А, fruits_Б, fruits_В ….
# Важно! Обратите внимание, что нет фруктов, начинающихся с некоторых букв.
# Напишите универсальный код, который будет работать с любым списком фруктов
# и распределять по файлам в зависимости от первых букв, имеющихся в списке фруктов.
# Подсказка:
# Чтобы получить список больших букв русского алфавита:
# print(list(map(chr, range(ord('А'), ord('Я')+1))))
