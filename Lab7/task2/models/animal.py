
class Animal:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def make_sound(self):
        pass

    def birthday(self):
        self.age += 1
        return f"Happy birthday, {self.name} You're now {self.age} years old."

    def __str__(self):
        return f"This is {self.name}, and is {self.age} years old and it's {self.color}"