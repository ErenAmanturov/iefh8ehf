ten = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = list(filter(lambda x: x % 2 == 0, ten))
print(list(map(lambda x: x**2, evens)))


def index(lis=ten):
    while True:
        try:
            h = (input('Введите индекс: '))
            if h == 'exit':
                print('Finished')
                break
            print(f'{lis[h]}')
        except:
            print(f'Актуальные индексы: от 0 до {len(lis) - 1}')
dddd]

you = [i for i in range(1, 64)]

index(you)
