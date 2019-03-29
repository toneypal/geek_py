# toneypal - Antonina Palchikova

# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Решите задачу, используя только две переменные.
# Подсказки:
# * постарайтесь сделать решение через действия над числами;
#
# user_input_1 = ''
# user_input_2 = ''

input_list = []

print("Введите первое число:")
input_list.append(input())


print("Введите второе число:")
input_list.append(input())

user_input_1 = input_list[1]
user_input_2 = input_list[0]


print("Поменяем значения переменных местами%", user_input_1, user_input_2)
