class ComplexNumber:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        a = self.a + other.a
        b = self.b + other.b
        return ComplexNumber(a, b)

    def __mul__(self, other):
        a = (self.a * other.a) - (self.b * other.b)
        b = (self.a * other.a) + (self.b * other.b)
        return ComplexNumber(a, b)

    def __str__(self):
        return f"{self.a} + {self.b}i"


x = ComplexNumber(2, 7)
y = ComplexNumber(3, 8)
summ = x + y
mult = x * y

print(x)
print(y)
print(summ)
print(mult)