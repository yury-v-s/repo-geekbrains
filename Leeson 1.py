# Задание 1
var_1 = 10
var_2 = "text"
print(var_2, var_1)
var_1 = input("Введите любой текст ")
var_2 = int(input("ВВедите целое число "))
print(f"Преобразовали переменные с одного типа на другой {var_2}, {var_1}")
# Задание 2
user_input = int(input("Введите целое число секунд: "))
var_hours = user_input // 3600
var_minute = user_input % 3600 // 60
var_second = user_input % 3600 % 60
print(f"{'%0.2d' % var_hours}:{'%0.2d' % var_minute}:{'%0.2d' % var_second}")
# Задание 3
user_input = (input("Введите целое число:"))
n = int(user_input)
nn = int(user_input + user_input)
nnn = int(user_input + user_input + user_input)
print(n + nn + nnn)
# Задание 4
user_input = int(input("Введите целое число: "))
max_number = 0
while user_input > 0:
    if max_number < user_input % 10:
        max_number = user_input % 10
    user_input = user_input // 10
print(max_number)
# Задание 5
company_proceeds = int(input("Введите сумму выручки компании: "))
company_costs = int(input("Введите сумму издержек компании: "))
if company_proceeds <= company_costs:
    print("Вы работаете в убыток")
else:
    comp_rent = (company_proceeds - company_costs) / company_proceeds * 100
    print(f"Рентабельность вашей компании составила {'%0.2f' % comp_rent}%")
    hr_count = int(input("Укажите количество сотрудников вашей компании: "))
    proc_hr = (company_proceeds - company_costs) / hr_count
    print(f"Каждый сотрудник зароботал для компании {'%0.2f' % proc_hr} денег.")
# Задание 6
a = int(input("Введите число a: "))
b = int(input("Введите число b: "))
i = 1
if a < b:
    while a <= b:
        i = i + 1
        a = a * 1.1
    print(i)
else:
    print(1)
