# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.


list = [1,2,3,4,5,6,7,8,9,1234,1234,34567,5678,89,345,567,78,89,0]

for i in list:
    if i % 2:
        print("i = ", i)
        i = i / 4
        print ("i/4 = ",i)
    else:
        i = i * 2
        print("i*2 = ", i)
