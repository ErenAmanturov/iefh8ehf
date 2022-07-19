class A:
    def __init__(self, num):
        self.num = num

    def __add__(self, num2):
        print('Dunder method __add__')
        self.num += num2
        return self.num

    def __mul__(self, num2):
        self.num *= num2
        return self.num

    def __sub__(self, num2):
        self.num -= num2
        return self.num

    def __floordiv__(self, num2):
        self.num //= num2
        return self.num

    def __str__(self):
        return self.num.__str__()


a1 = A(10)
print(a1)
