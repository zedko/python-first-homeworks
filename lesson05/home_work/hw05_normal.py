import os
import sys
import lesson05.home_work.hw05_easy as easy_lib

# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки ## воспользуюсь функцией из задания easy и выведу только папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py


def print_main_menu():
    print("-----------------------------")
    print("input number to do something")
    print("1 to change folder")
    print("2 to see folders in current directory")
    print("3 to delete a folder")
    print("4 to create a folder")
    print("exit to stop")
    print("-----------------------------")


def all_actions(input_value):
    if input_value in ("1", "2", "3", "4"):
        if input_value == "1":  # change directory
            new_dir = os.path.join(os.getcwd(), (input("input directory:    ")))
            try:
                os.chdir(new_dir)
                print("Success. Directory changed to: ", os.getcwd())
            except:
                return print("Something went wrong. Could not reach that directory. Self destruction starting in 5 sec...")
        if input_value == "2":  # show directory
            print("Success. Folders in current dir:   ")
            easy_lib.show_folders()
        if input_value == "3":  # delete a folder
            del_dir = os.path.join(os.getcwd(), (input("input directory name to delete it:   ")))
            try:
                easy_lib.delete_dir(del_dir)
                print("Success. Directory deleted")
            except:
                return print("Something went wrong. Could not delete the file. Self destruction starting in 5 sec...")
        if input_value == "4":  # create a folder
            dir_prefix = input("Input a name for a folder:   ")
            try:
                easy_lib.create_dir(dir_prefix)
                print("Success", easy_lib.show_folders())
            except:
                print("Something went wrong. Could not create that file. Self destruction starting in 5 sec...")
                return
    else:
        print("Check your input and start again")
        return


current_input_value = "0"
while current_input_value is not "exit":
    print_main_menu()
    current_input_value = input("go ahead:    ")
    if current_input_value == "exit":
        print("Chao")
        break
    all_actions(current_input_value)
