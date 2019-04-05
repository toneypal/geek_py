# Постарайтесь использовать то, что мы прошли на уроке при решении этого ДЗ,
# вспомните про zip(), map(), lambda, посмотрите где лучше с ними, а где они излишни!

# Задание - 3
# Создайте функцию, принимающую неограниченное количество строковых аргументов,
# верните самую длинную строку из полученных аргументов

# def maximum_str(*args):
#     print(max(args))
#     return max(args)

# unlimits_strings = ['Антонина','аля','Галя','Наташа','c']

def max_length(*args):

    str_copy = ''
    str_max = []
    # for str in unlimits_strings:
    for arg in args:
        if len(arg) > len(str_copy):

            # str_max.append(str)

            str_copy = arg
        else:
            pass

    return str_copy

print(max_length('Антонина', 'аля', 'Галя', 'Наташа', 'asdfghjklkjhgfdsa'))