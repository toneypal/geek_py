# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.


list_1 = ['a', 1, 'b', 3, 'c', 2, 3, 6, 'f']
list_2 = ['a', 4, 'b', 3, 'c', 2]

for i in list_2:
    for j in list_1:
        if j in list_2:
            list_1.remove(j)

print("list_1 = ",list_1)
