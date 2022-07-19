low = 0
high = 100
tries = 0
m = 50
k = f'Загадайте число от 0 до 100.\nЕсли цифра угадана - да\nЕсли загаданная цифра больше - >\nВ другом случае - <'
print(k)
n = input('Загадайте число: ')


with open('result.txt', 'w', encoding='UTF-8') as file:
    file.write('Попытки: ')
    while True:
        print(f'Ваше загаданное число равно {m}?')
        tries += 1
        answer = input()
        file.write(f'{m} ')
        if answer == '>':
            low = m
            m = (low + high) // 2
        elif answer == '<':
            high = m
            m = (low + high) // 2
        elif answer.lower() == 'да':
            print(f'Ваше загаданное число это: {m}')
            file.write(f"\nКоличество попыток: {tries}")
            file.write(f"\nЗагаданное число: {m}")
            break
        else:
            print('Если цифра угадана - да\nЕсли загаданная цифра больше - >\nВ другом случае - <')
