ten = [i for i in range(1, 11)]
evens = list(filter(lambda x: x % 2 == 0, ten))
print(list(map(lambda x: x**2, evens)))


def index(lis=ten):
    while True:
        try:
            h = (input('Введите индекс: '))
            if h == 'exit':
                print('Finished')
                break
            print(f'{lis[int(h)]}')
        except:
            print(f'Актуальные индексы: от 0 до {len(lis) - 1}')


you = [i for i in range(1, 64)]

index(you)
