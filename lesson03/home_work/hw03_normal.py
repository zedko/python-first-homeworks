# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

# first = int(input("Введите нижний диапазон чисел Fибоначчи: "))
# second = int(input("Введите верхний диапазон чисел Fибоначчи: "))


def fibonacci(n, m):
    fib_num = [1, 1]
    for x in range(1, m):
        fib_num.append(fib_num[x] + fib_num[x - 1])
    return fib_num[n:m]
    pass


print(fibonacci(0, 15))


# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):
    new_list = []
    while origin_list.__len__() != 0:
        min_num = origin_list[0]
        for x in range(origin_list.__len__()):
            if min_num > origin_list[x]:
                min_num = origin_list[x]
        new_list.append(min_num)
        origin_list.remove(min_num)
    return new_list


print(sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))


# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.


def new_filter(base_function, base_list):
    new_list = []
    for x in range(base_list.__len__()):
        if base_function(base_list[x]) is True:
            new_list.append(base_list[x])
    return new_list
    pass


print("Результат работы дешевой подделки: ")
print(new_filter(lambda i: i == "one", ["one", "two", "one", "one", "two", "three", "one", "one", "two"]))
print("Неповторимый оригинал: ")
print(list(filter(lambda i: i == "two", ["one", "two", "one", "one", "two", "three", "one", "one", "two"])))


# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

