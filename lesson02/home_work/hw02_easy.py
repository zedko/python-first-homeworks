# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()
print("#1")
fruits = ["apple", "banana", "kiwi", "watermelon"]

for x in range(0, fruits.__len__()):
    print("{0}. {1:>15}".format(x, fruits[x]))


# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

print(" ")
print("#2")
data1 =[]
data2 =[]
filler = "empty"
# наполняем списки
while filler != "end":
    filler = input("Input next element or ""end"": ")
    if filler == "end":
        print(data1)
        break
    else:
        data1.append(filler)
filler = "empty"
while filler != "end":
    filler = input("Input next element or ""end"": ")
    if filler == "end":
        print(data2)
        break
    else:
        data2.append(filler)
# удаляем лишние элементы. Есть проблема в данном решении, удалятся дубли в списке один, даже если их нет в списке 2.
answer = set(data1).difference(set(data2))
print("Answer ", answer)


# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

print(" ")
print("#3")
data3 = []
# наполняем список целыми числами
filler = "empty"
while filler != "end":
    filler = input("Input next integer or ""end"": ")
    if filler == "end":
        print("Your input is: ",data3)
        break
    else:
        data3.append(int(filler))
data4 = []
# заполнение нового списка по порядку модифицированными значениями
for i in range(0, data3.__len__()):
    if data3[i] % 2 == 0:
        data4.append(data3[i] / 4)
    else:
        data4.append(data3[i] * 2)
print(data4)


