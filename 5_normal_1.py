# toneypal - Antonina Palchikova
# Программа робот-помощник-информатор


# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py


# import os
# import sys
# import platform

import os.path

answer = ''
FILE_LIST_IN_DIR = os.listdir()
DICT_CHOICES = {
    "0": "Узнать текущий каталог:",
    "1": "Перейти в папку",
    "2": "Просмотреть содержимое текущей папки",
    "3": "Создать папку",
    "4": "Удалить папку"
}

while answer != 'q':
    answer = input( "\n хотите поработать? [y/n/q]" )

    try:
        if answer == 'y':
            print( "Тогда выберете из списка:" )
            for key, action in DICT_CHOICES.items():
                print( "__________________", key, action )

            choice = input( "Введите ваш выбор:" )
            print( type( int( choice ) ), type( choice ) )
            if choice in DICT_CHOICES.keys():

                if int( choice ) == 0:
                    print( "Узнать текущий каталог: ", os.getcwd())

                elif int( choice ) == 1:
                    print( "Введите путь к папке в формате: ")
                    dir_name = input()

                    if os.path.exists( dir_name ):
                        os.chdir( dir_name )
                        print( "Текущий каталог: ", os.getcwd())

                elif int( choice ) == 2:
                    for elem in os.listdir( os.getcwd()):
                        print( "__________________", elem)

                elif int( choice ) == 3:
                    new_dir = input( "Введите имя директории: ")
                    new_dir_path = input( "Введите путь, где будет создана указанная директория: ")
                    if not os.path.exists( new_dir_path + new_dir ):
                        os.chdir( new_dir_path)
                        try:
                            os.mkdir( new_dir)
                            print( "Успешно")
                        except Exception as e:
                            print( e)

                elif int( choice ) == 4:
                    print( "Какую папку Вы хотели бы удалить? Введите путь до этой папки: ")
                    dir_del_path = input( "Введите путь до этой папки: ")
                    if os.path.exists( dir_del_path ):
                        try:
                            os.remove( dir_del_path )
                            print( "Файл успешно удален" )
                        except Exception as e:
                            print( e )
                    else:
                        print( f'Я не смог найти файл {dir_del_path}')

        elif answer == 'n':
            print( "Good bay!" )
            exit()
        elif answer == 'q':
            exit()
        else:
            print( "Answer is not recognized" )

    except Exception as e:
        print( "Некорректный ввод!" )
        print( f'e = {e} /n trace: {e.with_traceback()}')
