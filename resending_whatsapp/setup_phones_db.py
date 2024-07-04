import random

# Список с 10 случайными именами
names = [
    "Анна",
    "Виктор",
    "Дмитрий",
    "Лев",
    "Константин",
]

# Телефонный номер
phone = "+79159329250"

# Запись в файл "phones.txt"
with open("phones.txt", "w") as file:
    for name in names:
        file.write(f"{phone},{name}\n")

print("Файл 'phones.txt' успешно создан.")
