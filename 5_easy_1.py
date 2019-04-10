# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os

for i in range(9):
    os.makedirs('dir_' + str(i + 1))

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

dirs_and_files = os.walk('/Users/aapalchikova/PycharmProjects/geek_py/geek_py/')
list1 = [elem for elem in dirs_and_files]
print(list1[0][1])

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

from shutil import copyfile

FILE_LIST_IN_DIR = os.listdir()

run_script_file = os.path.basename(__file__)
if run_script_file in FILE_LIST_IN_DIR:
    new_file = run_script_file + '(1)'
    print('src', os.path.abspath(run_script_file))
    print('dist', os.path.abspath(new_file))

copyfile(os.path.abspath(run_script_file),
         os.path.abspath(new_file) + new_file)

if new_file in FILE_LIST_IN_DIR:
    print("Файл успешно скопировался")
    print('Копия запущенного файла: ', new_file)
else:
    print('error')

