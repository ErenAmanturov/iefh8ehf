# Функции, аргументы: *args, **kwargs.

# def greeting():
#     print('Hello World!')
#
# greeting()
# def is_even(number):
#     if number % 2 == 0:
#         return True
#     else:
#         return False
# print(is_even(5))
# print(is_even(3))

# numbers = [1, 2, 3, 4,5,  6, 7, 8]
#
# def find_5(lst):
#     for i in lst:
#         print(i)
#         if i == 5:
#             return True
#     # if 5 in lst:
#     #     return True
#     return False
# #
# print(find_5(numbers))

# print(numbers)
# print(deleted)
# def plus(*args):
#     c = 0
#     result = 0
#     while c != len(args):
#         result += (args[c] * args[c+1])
#         c += 1
#         return result
#
# print(plus(8, 2, 5, 5))


# def greeting(name='qwerty', surname='Jack'):
#     # print(f'Hello, {name}!')
#     return f'Hello, {name} {surname}!'
#
# data = greeting()
#
# print(data)
#
# print(type(greeting('samat')))


# def get_square(width, length):
#     square = width * length
#     return square
#
#
# kitchen = get_square(3, 5)
# hall = get_square(5, 7)
# bedroom = get_square(4, 5)
#
# prices = {
#     'ленолеум': 250,
#     "ковер": 450,
#     'ламинат': 350
# }
#
#
# def get_price(square, price):
#     return square * price
#
#
# data = [
#     get_price(kitchen, prices['ленолеум']),
#     get_price(hall, prices['ковер']),
#     get_price(bedroom, prices['ламинат'])
# ]
#
# print(max(data))
#
#
#
#
#
# width = 3
# length = 4
# square_kitchen = width * length
# print(square_kitchen)
# width = 5
# length = 7
# square_hall = width * length
# print(square_hall)
