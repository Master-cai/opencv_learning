class orange:
    def __init__(self, weight, color):
        self.weight = weight
        self.color = color
        print('created a %dg %s orange!' % (weight, color))


a = orange(200, 'yellow')
print(a.color)
print(a.weight)
a.weight = 300
print(a.weight)
