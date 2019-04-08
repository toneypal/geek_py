# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

fruits_1 = ["apple", "banana", "kiwi"]
fruits_2 = ["apricot", "banana", "orange", "apple"]
fruits_3 = []

res = [i for i in fruits_1 if i in fruits_2]
print (res)
