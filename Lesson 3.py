# Задание 1

def div(v_1, v_2):
    try:
        v_1, v_2 = int(v_1), int(v_2)
        div_v = v_1 / v_2
    except ValueError:
        return "Ошибка, введите число"
    except ZeroDivisionError:
        return "Ошибка, делить на нОль нельзя"
    return round(div_v, 4)

print(div(input("ВВедите делимое - "), input("ВВедите делитель - ")))

# Задание 2

def user_info(name, surname, birthday, city, mail, phone):
    return f"Имя - {name}; Фамилия - {surname}; День рождения - {birthday}; Город - {city}; Почта - {mail};" \
            f" Телефон - {phone} "

print(user_info(name="Юрий", surname="С.", birthday="08.10.1985", city="Москва", mail="report_spam@inbox.ru",
                phone="+7(123)456-78-90"))

# Задание 3

def my_func(n_1, n_2, n_3):
    return sum(sorted([n_1, n_2, n_3])[1:])

print(my_func(9, 3, 7))

# Задание 4

def my_func(x, y):
    result = x ** y
    return result

print(my_func(10.6, -2))

# Задание 5

# Задание 6