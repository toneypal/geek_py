# Задание - 1
# Вам даны 2 списка одинаковой длины, в первом списке имена людей, во втором зарплаты,
# вам необходимо получить на выходе словарь, где ключ - имя, значение - зарплата.
# Запишите результаты в файл salary.txt так, чтобы на каждой строке было 2 столбца,
# столбцы разделяются пробелом, тире, пробелом. в первом имя, во втором зарплата, например: Vasya - 5000
# После чего прочитайте файл, выведите построчно имя и зарплату минус 13% (налоги ведь),
# Есть условие, не отображать людей получающих более зарплату 500000, как именно
#  выполнить условие решать вам, можете не писать в файл
# можете не выводить, подумайте какой способ будет наиболее правильным и оптимальным,
#  если скажем эти файлы потом придется передавать.
# Так же при выводе имя должно быть полностью в верхнем регистре!
# Подумайте вспоминая урок, как это можно сделать максимально кратко, используя возможности языка Python.


names = ['Лера', 'Мурад', 'Паша В.', 'Айгуль', 'Дима']
sellary = [280000, 500000, 850000, 150000, 250000]

# dict = {'Рома': 450000}
dict = {}

# for name in names:
#     for sel in sellary:

# for key in dict.keys():
#     for value in dict.values():

        # dict = map(dict.keys(), name)


for key_names, value_names in enumerate(names):
    for key, value in dict.items():
        dict[key] = value_names

for key_sellary, value_sellary in enumerate(sellary):
    for key, value in dict.items():
        dict[value] = value_sellary

print(dict)

# for key, value in enumerate(sellary):
#     dict[value] = value
#     # print(dict)
#
# for key,value in dict.items():



        # for name in names:
        #     for sel in sellary:
        #         # dict.update(name,sel)
        #         # map(dict, names, sellary)
        #         # print (dict)
        #         key = name
        #         value = sel

                # name = dict.keys()
                # sel = dict.values()
                # dict = map(dict, names, sellary)



#
# for key in dict.keys():
#     for value in dict.values():
#         key = names[key]
#         print(key)
#         print(key)
#         value = sellary[value]
#         print(value)


# print (dict)