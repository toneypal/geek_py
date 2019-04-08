
# Эти задачи необходимо решить используя регулярные выражения!

# Задача - 1
# Запросите у пользователя имя, фамилию, email.
# Теперь необходимо совершить проверки, имя и фамилия должны иметь заглавные первые буквы.
# email - не должен иметь заглавных букв и должен быть в формате: текст в нижнем регистре,
# допускается нижнее подчеркивание и цифры, потом @, потом текст, допускаются цифры, точка, ru или org или com.
# Например:
# Пупкин василий - неверно указано имя, te$T@test.net - неверно указан email
# (спецсимвол, заглавная буква, .net), te_4_st@test.com - верно указан.

import  re

print("Введите имя: ")
name = input()
print("Введите фамилию: ")
surname = input()
print("Введите email :")
email = input()

pattern_name = '[(A-Z)][(a-z+]'
pattern_email = '[a-z_0-9]+@[a-z_0-9]+\.(com|org)'

while True:

    if re.match (pattern_name, name):
        print("Имя ведено верно")

    elif re.match (pattern_name, surname):
        print("Фамилия ведена верно")

    elif re.match(pattern_email, email):
        print("email ведено верно")
        break
    else:
        print("Имя должна иметь заглавные первые буквы ")
        print("Введите в формате: /n Tекст в нижнем регистре, допускается нижнее подчеркивание и цифры ")
        break
