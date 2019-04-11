
# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <full_path or relative_path> - меняет текущую директорию на указанную
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.

# P.S. По возможности, сделайте кросс-платформенную реализацию.




# Узнать текущий каталог:
# os.getcwd()
# '/home/pl/Documents/python'

# Создать каталог:
#
# >>> os.mkdir('TEXT')
# Создать дерево каталогов:
#
# >>> os.makedirs('ONE/TWO/THREE')
# >>> os.listdir('ONE')
# ['TWO']
# >>> os.listdir('ONE/TWO')
# ['THREE']
# Список содержимого каталога (нерекурсивный):
#
# >>> os.listdir()
# ['text4.txt', 'text1.txt', 'text3.txt', 'try_except.py', 'files.py', 'text5.txt', 'grades_oop.py', 'grades.py', 'text6.txt', 'text2.txt', 'text.txt', 'TEXT']
# >>> os.listdir('/home')
# ['pl']
# Сведения о файле|каталоге:
#
# >>> os.stat('/home')
# posix.stat_result(st_mode=16877, st_ino=1048577, st_dev=2053, st_nlink=3, st_uid=0, st_gid=0, st_size=4096, st_atime=1344368518, st_mtime=1339316982, st_ctime=1339316982)
# >>> os.stat('text.txt')
# posix.stat_result(st_mode=33188, st_ino=1575740, st_dev=2053, st_nlink=1, st_uid=1000, st_gid=1000, st_size=41, st_atime=1344124896, st_mtime=1343895362, st_ctime=1343895362)
# Переименовать файл|каталог:
#
# >>> os.rename('text2.txt', 'xett.txt')
# >>> os.rename('TEXT', 'ETXT')
# Удаление каталога:
#
# >>> os.rmdir('ETXT')
# Смена текущего каталога:
#
# >>> os.chdir('/home')
# >>> os.getcwd()
# '/home'
# >>> os.chdir('./pl/Documents/python')
# >>> os.getcwd()
'/home/pl/Documents/python'