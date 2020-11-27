# Task 1


from sys import argv


def wage():
    try:
        name = argv[0]
        time, rate, prize = map(float, argv[1:])
        print("Имя программы: ", name)
        print(f"Сотрудник отработал - {time} ч.")
        print(f"Его ставка - {rate} р.")
        print(f"Премия составляет - {prize} р.")
        print(f"В этом месяце сотрудник получит - {time * rate + prize} р.")
    except ValueError:
        print("Используйте только числа для ввода")


wage()

# Task 2


my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print(my_list)
new_list = [my_list[num] for num in range(1, len(my_list)) if my_list[num - 1] < my_list[num]]
print(new_list)

# Task 3


my_list = [el for el in range(20, 241) if el % 20 == 0 or el % 21 == 0]
print(my_list)

# Task 4


from random import randint

my_list = [randint(0, 20) for i in range(25)]
print(my_list)
new_list = [el for el in my_list if my_list.count(el) == 1]
print(new_list)

# Task 5


from functools import reduce


def my_list(var1, var2):
    return var1 * var2


new_list = [el for el in range(100, 1001, 2)]
print(f"Произведение все четных чисел из диапозона [100:1000]:\n{new_list}\n = \n{reduce(my_list, new_list)}\n")

# Task 6a


from itertools import count

print("Программа генерирующая  целые числа, начиная с указанного, проход по сгенерированному списку по Enter,"
      " для выхода 'q'!")
for num in count(int(input("ВВедите число: "))):
    print(num, end=" ")
    f_ex = input()
    if f_ex.upper() == "Q":
        break

# Task 6b


from itertools import cycle

print("Программа повторяющая элементы некоторого списка, определенного заранее. Проход по сгенерированному списку по "
      "Enter, для выхода 'q'!")

for i in cycle(input("ВВедите список элементов через пробел: ").split()):
    print(i, end=" ")
    f_ex = input()
    if f_ex.upper() == "Q":
        break


# Task 7


def factorial(user_input):
    var = 1
    for i in range(1, user_input + 1):
        var = var * i
        yield f'{i}! = {var}'


for el in factorial((int(input("ВВедите число: ")))):
    print(el)
