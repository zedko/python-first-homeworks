# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать 
# в неограниченном кол-ве классов свой определенный предмет. 
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.


class Teacher(object):
    t_name: str  # FIO
    subject: str  # chemistry

    def __init__(self, name, subj):
        self.t_name = name
        self.subject = subj


class Student(object):
    s_name: str  # FIO
    group: str  # 7A
    father_name: str  # Alex
    mother_name: str  # Olga
    

    def __init__(self, name, group, father, mother):
        self.s_name = name
        self.group = group
        self.father_name = father
        self.mother_name = mother

    def get_student_group(self):
        return self.group

# class Learning(Teacher, Student):


stud_1_test = Student("Sergey Bodrov", "7A", "Alexey", "Yulya")
stud_2_test = Student("Jenya Ivanova", "7A", "Ivan", "Olesya")
stud_3_test = Student("Daniil Rostkov", "6B", "Nikolai", "Irina")
student_list = [stud_1_test, stud_2_test, stud_3_test]


def add_student():  # дополнение списка для тестов
    name = input(str("Name: "))
    group = input(str("Group: "))
    father = input(str("Father: "))
    mother = input(str("Mother: "))
    student_list.append(Student(name, group, father, mother))


while True:
    question = input(str("Do you want to add a student? Y/N:  "))
    if question == "Y":
        add_student()
    else:
        break

print(student_list)


def get_groups():
    groups = set([x.get_student_group() for x in student_list])
    return groups


def get_students_in_group(group):

    pass

def get_student_lessons(student_name):
    pass
def get_student_parents(student_name):
    pass
def get_group_teachers(group):
    pass

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика 
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе


print("All groups:", get_groups())
