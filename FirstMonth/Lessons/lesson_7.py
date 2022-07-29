# lambda, и работа с исключениями
# lambda arguments: expression
# students_in_class = [18, 20, 14, 3, 8, 19, 12, 7, 2, 21, 5]
#
# students = {'abdulla': 5,
#             'adilet': 5,
#             'nazira': 5,
#             'ali': 4,
#             'aleksandr': 5,
#             'bekzat': 2,
#             'almaz': 2,
#             'kuttubai': 2,
#             'eren': 5,
#             'azamat': 2,
#             'amir': 4,
#             'ulan': 4,
#             'aitegin': 2}
#
# while len(students_in_class) != 0:
#     print(students_in_class)
#     try:
#         id_s = int(input('введите номер: '))
#         name = input('введите имя: ')
#         rate = int(input(f'введите оценку для {name}'))
#         if name in students.keys():
#             students[name] += rate
#         else:
#             students[name] = rate
#         students_in_class.remove(id_s)
#     except ValueError:
#         print('Вводите только числа!')
#
# for k in students:
#     print(k)



# numbers = [1, 2, 3]
# while True:
#     try:
#         ind = int(input('введите индекс!'))
#         print(numbers[ind])
#     except:
#         print('такого индекса нет! или вводите только числа')
        # print("вводите только числа")
    # except ValueError:



# a = lambda x, c: x * c**2**2
#
# print(a(5, 2))



# n = int(input('введите число: '))



# print(word)



# numbers = [i for i in range(1, 11)]
# new = list(filter(lambda x: x % 2 != 0, numbers))
# print(new)
# print([i for i in numbers if i % 2 != 0])

# other = list(map(lambda x: x - 1, new))
# object = list(sorted(numbers, reverse=True))



# print(object)
# print(numbers)
# print(other)
# lambda_func = lambda a, b, c: a + b * c
# print(lambda_func(2, 3, 4))



# def up_letter(word):
#     return word.upper()


# def up_word(lst, func):
#     for i in lst:
#         print(func(i))
#
#
# words = ['books', 'item', 'sport']
#
# # up_word(words, up_letter)
# up_word(words, lambda x: x.title())
# abdulla
# adilet
# nazira 11
# ali 4
# aleksandr 7
# bekzat 5.5
# almaz 7
# kuttubai 4.5
# eren 10
# azamat 4
# amir
# ulan
# aitegin 4.5
# denis 2
# sairagul 4
# abdurahim 4
# kasiet 3
