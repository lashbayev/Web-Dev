from animal import Animal

class Dog(Animal):
    def __init__(self, name, age, color, breed, sound = "Woof"):
        super().__init__(name, age=age, color=color)
        self.breed = breed
        self.sound = sound

    def make_sound(self):
        return f"{self.name} barks loudly and says {self.sound}"
    
    def fetch(self, item = "stick"):
        return f"{self.name} catches {item}"
    
    def __str__(self):
        return f"This is {self.name}, and is {self.age} years old and it's {self.color} and it is dog of type {self.breed}"
    
    
