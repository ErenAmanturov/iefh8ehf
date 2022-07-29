def _1_word(n='Hello World!'):
    if type(n) != str:
        return False
    else:
        word = n.split()
        return word[0]
print(_1_word())

def avrsum(*numbers):
    return sum(numbers) // len(numbers)
print(avrsum(2, 4))

def password(n):
    if len(n) >= 6 and not n.isalpha() and not n.isdigit() \
            and n[0] and n.isalnum():
        return True
    return False

print(password('1234asf&'))
