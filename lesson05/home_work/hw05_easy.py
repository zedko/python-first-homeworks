import os
import sys


# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

curr_dir = os.getcwd()


def create_dir(dir_prefix: str = "dir", dir_amount: int = 1):
    if dir_amount == 1:
        dir_names = [dir_prefix]  # a single directory
    else:
        dir_names = [dir_prefix+str(x) for x in range(int(dir_amount))]  # generate names for many directories
    for i in dir_names:  # creating dirs
        os.mkdir(os.path.join(curr_dir, i))


def delete_dir(dir_prefix: str = "dir", dir_amount: int = 1):
    if dir_amount == 1:
        dir_names = [dir_prefix]  # a single directory
    else:
        dir_names = [dir_prefix+str(x) for x in range(int(dir_amount))]  # generate names for many directories
    for i in dir_names:  # deleting dirs
        os.rmdir(os.path.join(curr_dir, i))




# create_dir(10)
# delete_dir(10)
# print(curr_dir, dir_names)


# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
def show_folders():
    dir_index = 0
    list_all = os.listdir(curr_dir)  # get files and dir in current dir
    for x in list_all:
        if os.path.isdir(x):
            dir_index += 1
            print(dir_index, "...", x)


# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

def copy_main_file():
    if __name__ == "__main__":
        from shutil import copyfile
        current_file = __file__
        new_file_name = str(current_file[:-3]+"_copy.py")
        copyfile(current_file, new_file_name)


