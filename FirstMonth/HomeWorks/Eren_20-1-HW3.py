all = 'qwertyuihopasdfgjklzxcvbnmцукенгшщзхйъфывапролджэячсмитьбю'
all_gl = 'eioaуеыаоэяию'
while True:
    word = input()
    word2 = word
    word = word.lower()
    gl = 0
    sogl = 0
    kol = 0
    for i in word:
        if i in all:
            kol += 1
            if i in all_gl:
                gl += 1
            else:
                sogl += 1
    if word == 'exit':
        print('Программа завершена')
        break
    print(f'Слово: {word2}')
    print(f'Количество букв: {kol}')
    print(f'Согласных букв: {sogl}')
    print(f'Гласных букв: {gl}')
    print(f'Гласные/Согласные: {round(gl / kol * 100, 2)}% / {round(sogl / kol * 100, 2)}%')