class Shape:
    def __init__(self, w, l):
        self.width = w
        self.lengh = l

    def print_size(self):
        print('''{} by {} 
        '''.format(self.width, self.lengh))


class Square(Shape):
    def area(self):
        return self.width * self.lengh
    def print_size(self):
        print('''I am {} by {} 
                '''.format(self.width, self.lengh))

square = Square(20, 20)
square.print_size()