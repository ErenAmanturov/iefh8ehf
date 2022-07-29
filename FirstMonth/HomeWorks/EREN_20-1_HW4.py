data_tuple = ('h', 6.13, 'C', 'e', 'T', True, 'k', 'e', 3, 'e', 1, 'g')
letters = []
numbers = []

for i in data_tuple:
    if type(i) == str or type(i) == bool:
        letters.append(i)
    else:
        numbers.append(i)
print(numbers)
del numbers[0]
print(numbers)
numbers.sort()
print(numbers)
numbers.insert(1, 2)
print(numbers)
print(letters)
letters.append(letters.pop(4))
print(letters)
letters.reverse()
print(letters)
numbers[1], numbers[2] = 4, 9
letters[1], letters[-2] = 'G', 'c'

letters = tuple(letters)
numbers = tuple(numbers)
print(letters)
print(numbers)
