# toneypal - Antonina Palchikova

# Задача-2: Запросите от пользователя число, сохраните в переменную,
# прибавьте к числу 2 и выведите результат на экран.
# Если возникла ошибка, прочитайте ее, вспомните урок и постарайтесь устранить ошибку.


def addition(number):
    number_plus_2 = number + CONST
    print("number_plus_2 =", number_plus_2)


CONST = 2

print("Введите число:")
number = input()
if type(number) is 'int':
    addition(number)

else:
    try:
        number = int(number)
        addition(number)
    except:
        print("Вы ввели не число!")