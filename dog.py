class Dog:
    def __init__(self, name):
        self.name = name
        self.tricks = []

    def get_name(self):
        print(self.name)

    def sit(self):
        print(self.name + " sits.")
        if "sit" not in self.tricks:
            self.tricks.append("sit")

    def high5(self):
        print(self.name + " gives you a high five!")
        if "high five" not in self.tricks:
            self.tricks.append("high five")

    def cartwheel(self):
        print(self.name + " does a cartwheel!?!?")
        if "cartwheel" not in self.tricks:
            self.tricks.append("cartwheel")

dog = Dog()

dog.get_name()
dog.sit()
dog.high5()
dog.cartwheel()

print(dog.tricks)


