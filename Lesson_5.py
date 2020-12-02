# Task 1


with open('Lesson_5_1.txt', 'w', encoding='utf-8') as doc1:
    while True:
        line = input('Введите информацию для записи, либо пусто для завершения: ')
        if not line:
            break
        print(line, file=doc1)

# Task 2


with open('Lesson_5_2.txt', 'r',  encoding='utf-8') as doc2:
    line = doc2.readlines()
    for i, v in enumerate(line, 1):
        count_words = len(v.split())
        print(f'Строка {i} состоит из {count_words} слов')

# Task 3


with open('Lesson_5_3.txt', 'r', encoding='utf-8') as doc3:
    user_dict = {line.split()[0]: int(line.split()[1]) for line in doc3}
    print(f'Меньше 20к получают след. сотрудники: {[el[0] for el in user_dict.items() if el[1] < 20000]}\n'
          f'Средняя зар. плата составляет: {round(sum(user_dict.values()) / len(user_dict), 2)}')

# Task 4

"""К сожалению своих мозгов не хватило для решения данной задачи, прибег к помощи"""
trans_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

with open('Lesson_5_4_rus.txt', 'w', encoding='utf-8') as doc4rus:
    with open('Lesson_5_4.txt', 'r', encoding='utf-8') as doc4:
        doc4rus.writelines([line.replace(line.split()[0], trans_dict.get(line.split()[0])) for line in doc4])

# Task 5


from random import randint

with open('Lesson_5_5.txt', 'w+', encoding='utf-8') as doc5:
    doc5.write(' '.join([str(randint(1,100)) for i in range(100)]))
    doc5.seek(0)
    print(sum(map(int, doc5.readline().split())))

# Task 6


user_dict = {}
with open('Lesson_5_6.txt', 'r', encoding='utf-8') as doc6:
    for line in doc6:
        line = line.replace(':', '').replace('—', '').replace('(л)', '').replace('(пр)', '').replace('(лаб)', '')\
            .replace('.', '')
        user_dict[line.split()[0]] = sum(map(int, line.split()[1:]))
    print(user_dict)

"""Task 7 не осилил пока"""


