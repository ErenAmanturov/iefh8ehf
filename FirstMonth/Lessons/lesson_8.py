import time
from random import randint


while True:
    a, b = randint(1, 9), randint(1, 9)
    result = a * b
    try:
        user_answer = int(input(f'сколько будет {a} * {b} ?'))
        if user_answer == 0:
            print('До свидания!')
            break
        if user_answer == result:
            with open('file.txt', 'a') as file:
                file.write(f'{a} * {b} = {user_answer} ({result}) правильно\n')
            print('ok!')
        else:
            print(f'неправильно! ({result})')
            with open('file.txt', 'a') as file:
                file.write(f'{a} * {b} = {user_answer} ({result}) неправильно\n')
    except:
        print('вводите только цифры до 81')



# file = open('text.py', 'w')
# file.write("today 8'th lesson")
# file.close()

# with open('new.txt', 'w') as file:
#     file.write('python')
#
# with open('file.txt', 'a') as file:
#     file.write('\nbishkek')

# with open('text.txt', 'r', encoding='UTF-8') as file:
#     for i in file.read():
#         time.sleep(0.2)
#         print(i, end='')
    # print(file.readlines()[:2])

