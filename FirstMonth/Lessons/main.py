import random
lst = ['камень', 'бумага', 'ножницы']
while True:
    bot = random.choice(lst)
    player = input('Введите (Введите (камень, бумага, ножницы, дино) -')
    if player =='выход':
        print("Программа завершена!")
        break
    if player == bot:
        print('Ничья!')
    elif (bot == "камень" and player == "ножницы") or (bot == "бумага" and player == "камень") or (bot == "ножницы" and player == "бумага"):
        print("бот выиграл!")
    elif (player == "камень" and bot == "ножницы") or (player == "бумага" and bot == "камень") or (player == "ножницы" and bot == "бумага"):
        print("игрок выиграл!")
    elif player == 'дино':
        print("игрок выиграл!")
    else:
        print("неправильная команда!")

