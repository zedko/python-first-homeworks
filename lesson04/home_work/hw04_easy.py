# Все задачи текущего блока решите с помощью генераторов списков!
import random


# Задание-1:
# Дан список, заполненный произвольными целыми числами. 
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]
list_one = [random.randint(-100, 100) for _ in range(8)]
print(list_one)
list_two = list_one.copy()
list_two = [i ** 2 for i in list_two]
print(list_two)


# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.
fruits_one = ["apple", "banana", "kiwi", "watermelon", "melon", "grapes", "pineapple", "peach", "plum"]
fruits_two = ["orange", "pear", "banana", "apricot", "apple", "melon", "чебурашка"]
fruits_united = fruits_one + fruits_two
fruits_three = list(filter(lambda x: fruits_united.count(x) > 1, fruits_united))  # Выделяем все фрукты с повторением
fruits_three = list(set(fruits_three))  # Удаляем дубли
print(fruits_three)


# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

# a_list = [random.uniform(-100, 10000) for _ in range(15)]
# с произвольными числами слишком маловероятнен шанс выполнения всех условий, используем randint
a_list = [random.randint(-100, 10000) for _ in range(15)]
print(a_list)
b_list = list(filter(lambda x: x % 3 == 0 and x > 0 and x % 4 != 0, a_list))
print(b_list)

