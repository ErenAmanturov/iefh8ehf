# 1:

def f_word(sentence='Hello word!'):
    if type(sentence) != str:
        return False
    else:
        word = sentence.split()
        return word[0]


print(f_word('11iu  gc'))


# 2:

def a_number(*arg):
    return int(sum(arg) / len(arg))


print(a_number(1, 2, 3))


# 3:
def pss_6(password):
    if len(password) >= 6 and not password.isalpha() and not password.isdigit() and password.isalnum():
        return True
    else:
        return False


print(pss_6('qwerty6'))
