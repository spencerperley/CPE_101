class Dog:
    def __init__(self, breed, size, color, age, name=None):
        self.breed = breed
        self.size = size
        self.color = color
        self. age = age
        self.name = name

    def bark(self):
        print("woof")

    def Name(self):
        if self.name:
            print(f"my name is {self.name}")

        else:
            print("sorry I dont have a name")

    def active(self):
        print(self)


