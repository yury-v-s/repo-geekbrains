# Задание 1
my_list = [(1 + 2j), 1, 2.4, False, 'String', [1, 2], (1, 2, 2.5), None, {1: 'one', 2: 'two'}, {1, 2},
           frozenset(), range(1), bytearray(b'one'), b'two', zip(*[(1, 2), (3, 4), ('a', 'b')]), TypeError]
for i, item in enumerate(my_list, 1):
    print(f"{i}.  {item} - {type(item)}")

# Задание 2
user_input = list(input("ВВедите число без пробелов: "))
for i in range(1, len(user_input), 2):
    user_input[0], user_input[i] = user_input[1], user_input[i - 1]
print(user_input)
# Задание 3
# Задание 4
# Задание 5
# Задание 6