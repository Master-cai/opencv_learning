class Always:
    def __init__(self, number):
        self.number = number

    def __add__(self, other):
        return self.number + other.number

x = Always(-20)
y = Always(10)

print(x + y)
