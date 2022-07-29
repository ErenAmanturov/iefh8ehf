# Калькулятор2

while True:
    try:
        c = input('What u want to do: +, -, *, /  ')
        a = float(input('First number: '))
        b = float(input('Second number: '))
        if c == '+':
            result = a + b
            print(result)
        elif c == '-':
            result = a - b
            print(result)
        elif c == '*':
            result = a * b
            print(result)
        elif c == '/':
            result = a / b
            print(result)
        else:
            print('You have exceeded limits of calculator!')
    except ZeroDivisionError:
        print('You cannot divide to 0')



