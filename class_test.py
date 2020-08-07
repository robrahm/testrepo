class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(f"{self.name} is now sittinggg.")

class Puppy(Dog):
    def __init__(self, name):
        super().__init__('name', 0)

    def pee(self):
        print(f"{self.name} is peeing")
