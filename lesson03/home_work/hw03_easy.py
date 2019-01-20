# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

# a = input("Введите число    ")
# b = input("Введите кол-во знаков после запятой   ")

def my_round(number, ndigits):
    divided_number = str(number).split(".")

    # определяем в какую сторону округлять по числу следующему за последним
    if int((divided_number[1])[:ndigits + 2]) >= 5:
        #ДОПИСАТЬ ОКРУГЛЕНИЕ ВВЕРХ, сейчас выполняется не корректно
        new_fract_part = int(divided_number[1]) + (10 ** ndigits)
    else:
        new_fract_part = int(divided_number[1])
    divided_number[1] = str(new_fract_part)
    # обрезаем дробную часть
    divided_number[1] = (divided_number[1])[:ndigits + 1]
    rounded_number = float(".".join(divided_number))
    return rounded_number
    pass



# print(my_round(a,b))



print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):
    if str(ticket_number).__len__() == 6:
        ticket_number_1_sum = 0
        ticket_number_2_sum = 0
        ticket_number_1 = list((str(ticket_number))[:3])
        ticket_number_2 = list((str(ticket_number))[3:])
        for x in range(3):
            ticket_number_1_sum += int(ticket_number_1[x])
            ticket_number_2_sum += int(ticket_number_2[x])
        if ticket_number_1_sum == ticket_number_2_sum != 0:
            return True
    pass


print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
print(lucky_ticket(436752))
