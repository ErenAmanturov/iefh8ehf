# dictionary, set (dict, set)
# {key: value}

# a = {
#      'Dog': 'sharik',
#      'Fish': 'Phorel'
# }

for k, v in a.items():
     print(f'{k} - {v}')

# students = [11, 21, 12, 3, 8, 13, 20, 5, 23]
# students1 = [11, 21, 12, 3, 8, 13, 2, (0, 5, 23)]
# result = {}
# while len(students) != 0:
#     print('задают вопрос', students1)
#     print('отвечают', students)
#     question_s = int(input('Спрашивает: '))
#     answer_s = int(input('Отвечает: '))
#     name = input(f'name: {answer_s}')
#     rate = int(input(f'оценка для {name}'))
#     result[name] = rate
#     students.remove(answer_s)
#     students1.remove(question_s)
#
# for name, rate in result.items():
#     print(f'{name}: {rate}')
#
# numbers = (1, 2, 3, 4, 5)
# words = ('one', 'two', 'three', 'four', 'five')

# dictionary = {}
# c = 0
# while len(dictionary) != len(numbers):
#      dictionary[numbers[c]] = words[c]
#      c += 1
# print(dictionary)

a = {1, 1,  2, 2,  3, 4, 5, 6, 7, 'Geek', 'Geek'}
print(a)

# plov = {'рис', "мясо", "морковь"}
# beshbarmak = {'мясо', "тесто", "лук"}
#
# print(plov.symmetric_difference(beshbarmak))
# print(plov ^ beshbarmak)
#
# print(plov.intersection(beshbarmak))
# print(plov & beshbarmak)
#
# print(plov.difference(beshbarmak))
# print(plov - beshbarmak)
#
# print(plov.union(beshbarmak))
# print(plov | beshbarmak)


# numbers = [(1, 2), (3, 1), (3, 3), (4, 2)]
#
# # numbers = set(numbers)
# numbers = dict(numbers)
# print(numbers)
# numbers1 = {1, 2, 3, 1, 3, 3, 4, 2, 1}
# letters = {'a', 'b', 'a', 'c', 1, 3, 1}
# letters.add(5)
#
# print(numbers)
# print(numbers1)
# print(type(numbers1))
# print(letters)

# student = {
#     'name': 'Jack',
#     'age': 20,
#     'friends': ['Sam', 'Alisa', 'Max', 'Adilet'],
#     'girlfriend': True
# }
#
# print(len(student))
#
# for k, v in student.items():
#     print(v, '-', k)

# print(student)
# print(student.keys())
# print(student.values())
# print(student.items())
#
# student['surname'] = 'Jack captain Sparrow!'
#
# del student['girlfriend']
# deleted = student['friends'].pop(0)
# # deleted = student.pop('friends')
#
# print(deleted)
# print(student)

# student['pets'] = 'rex'
# student['girlfriend'] = False
# student['friends'].append('Azamat')
# student['friends'][2] += ' Payne'


# student = {
#     'name': 'Jack',
#     23: [1, 2, 3],
#     (5, 6, 7): 'tuple',
#     True: False,
# }