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


fructs = ["яблоко", "банан", "киви", "арбуз"]

# print('фрукты в виде нумерованного списка'.format(*fructs))
j = 1
for i in fructs:
    print("{}. {}".format(j,i))
    j += 1

    #         print("{}.\t{:<5}\t{:>5}".format(index, value, num))


