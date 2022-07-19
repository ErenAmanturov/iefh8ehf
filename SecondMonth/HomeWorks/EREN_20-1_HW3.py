class Fraction:

    def __init__(self, numerator, denumerator):
        self.numerator = numerator
        self.denumerator = denumerator

    def GCD(self, a, b):
        return (self.GCD(b, a % b) if b else a)

    def __add__(self, other):
        denum = self.denumerator * other.denumerator // self.GCD(self.denumerator, other.denumerator)
        num = denum // self.denumerator * self.numerator +\
                denum // other.denumerator * other.numerator
        self.numerator = num
        self.denumerator = denum
        return Fraction(numerator=num, denumerator=denum)

    def __sub__(self, other):
        denum = self.denumerator * other.denumerator // self.GCD(self.denumerator, other.denumerator)
        num = denum // self.denumerator * self.numerator - \
                denum // other.denumerator * other.numerator
        self.numerator = num
        self.denumerator = denum
        return Fraction(numerator=self.numerator, denumerator=self.denumerator)

    def __mul__(self, other):
        num = self.numerator * other.numerator
        denum = self.denumerator * other.denumerator
        k = self.GCD(num, denum)
        num //= k
        denum //= k
        self.numerator = num
        self.denumerator = denum
        return Fraction(numerator=self.numerator, denumerator=self.denumerator)

    def __floordiv__(self, other):
        n = other.numerator
        other.numerator = other.denumerator
        other.denumerator = n
        num = self.numerator * other.numerator
        denum = self.denumerator * other.denumerator
        k = self.GCD(num, denum)
        num //= k
        denum //= k
        self.numerator = num
        self.denumerator = denum
        return Fraction(numerator=self.numerator, denumerator=self.denumerator)

    def __str__(self):
        return f"{self.numerator}/{self.denumerator}"


drob1 = input("Введите дробь в формате ?/?: ").split('/')
drob2 = input("Введите дробь в формате ?/?: ").split('/')

a = Fraction(int(drob1[0]), int(drob1[1]))
b = Fraction(int(drob2[0]), int(drob2[1]))

print(f"{drob1[0]}/{drob1[1]} + {drob2[0]}/{drob2[1]} = {a + b}")
a = Fraction(int(drob1[0]), int(drob1[1]))
print(f"{drob1[0]}/{drob1[1]} - {drob2[0]}/{drob2[1]} = {a - b}")
a = Fraction(int(drob1[0]), int(drob1[1]))
print(f"{drob1[0]}/{drob1[1]} * {drob2[0]}/{drob2[1]} = {a * b}")
a = Fraction(int(drob1[0]), int(drob1[1]))
print(f"{drob1[0]}/{drob1[1]} // {drob2[0]}/{drob2[1]} = {a // b}")
