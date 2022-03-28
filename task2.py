class Division:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        if self.b != 0:
            return f"{self.a/self.b}"
        else:
            return "You can't divide by zero!"


x = Division(int(input("Enter the first number: ")), int(input("Enter the second number: ")))
print(x)

