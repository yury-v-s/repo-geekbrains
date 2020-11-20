# Задание 1
user_list = [(1 + 2j), 1, 2.4, False, 'String', [1, 2], (1, 2, 2.5), None, {1: 'one', 2: 'two'}, {1, 2},
             frozenset(), range(1), bytearray(b'one'), b'two', zip(*[(1, 2), (3, 4), ('a', 'b')]), TypeError]
for i, item in enumerate(user_list, 1):
    print(f"{i}.  {item} - {type(item)}")

# Задание 2
user_input = list(input("ВВедите число без пробелов: "))
for i in range(1, len(user_input), 2):
    user_input[0], user_input[i] = user_input[1], user_input[i - 1]
print(user_input)

# Задание 3
user_input = int(input("ВВедите номер месяца: "))
month_dict = {1: "Январь", 2: "Февраль", 3: "Март", 4: "Апрель", 5: "Май", 6: "Июнь", 7: "Июль", 8: "Август",
              9: "Сентябрь", 10: "Октябрь", 11: "Ноябрь", 12: "Декабрь"}
month_list = ["Зима", "Зима", "Весна", "Весна", "Весна", "Лето", "Лето", "Лето", "Осень", "Осень", "Осень",
              "Зима"]
if 12 >= user_input > 0:
    print(f"{month_dict[user_input]}  - это {month_list[user_input - 1]} ")
else:
    print("Не правильно введен номер месяца!")

# Задание 4
user_input = input("ВВедите несколько слов: ").split()
for i, j in enumerate(user_input, 1):
    print(f"{i} {j[:10]}")

# Задание 5
user_list = [7, 5, 3, 3, 2]
print(f"Текущий ретинг {user_list}")
user_input = int(input("Введите новый элемент рейтинга: "))
i = 0
for n in user_list:
    if user_input <= n:
        i = i + 1
user_list.insert(i, float(user_input))
print(user_list)

# Задание 6
item = []
param = {"Название": "", "Цена": "", "Кол-во": "", "Ед. изм.": ""}
data = {"Название": [], "Цена": [], "Кол-во": [], "Ед. изм.": []}
i = 0
while True:
    if input('Для выхода "Q", "Enter" чтобы продолжить ').upper() == "Q":
        break
    i = i + 1
    for n in param.keys():
        user_input = input(f'ВВедите характеристику товара ({n}): ')
        param[n] = int(user_input) if (n == 'Цена' or n == 'Кол-во') else user_input
        data[n].append(param[n])
    item.append((i, param))
    print(f"\nСтруктура:\n{item}")
    print(f'Аналитика: ')
    for key, value in data.items():
        print(f'{key}: {value}')
