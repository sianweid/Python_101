# Klassen

# neue Klasse erstellen

class calculator():

    x = 0
    y = 0

    def __init__(self,x,y):
        self.x = x
        self.y = y


    def addition(self):
        added = self.x + self.y
        print(added)

    def substraction(self):
        sub = self.x - self.y
        print(sub)

    def multiply(self):
        mul = self.x * self.y
        print(mul)

    def divide(self):
        dev = self.x / self.y
        print(dev)


x = calculator(1,4)

print(x.addition())