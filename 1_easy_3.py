# toneypal - Antonina Palchikova

# Задача-3: Запросите у пользователя его возраст.
# Если ему есть 18 лет, выведите: "Доступ разрешен",
# иначе "Извините, пользование данным ресурсом только с 18 лет"

LIMIT = 18
print("Введите возраст:")
user_age = input()
try:
    if int(user_age) >= LIMIT:
        print("Доступ разрешен")
    else:
        print("Извините, пользование данным ресурсом только с 18 лет")
except:
    print("Вы ввели не число!")




