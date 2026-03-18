from animal import Animal

class Cat(Animal):
    def __init__(self, name, age, color, is_indoor, sound = "purr"):
        super().__init__(name, age=age, color = color)
        self.is_indoor = is_indoor
        self.sound = sound

    def make_sound(self):
        return f"{self.name} only meows and {self.sound}s still"
    
    def where_isit(self):
        location = "indoor" if self.is_indoor else "outside"
        return f"{self.name} is an {location} and meows there"
    
    def __str__(self):
        return f"This is {self.name}, and is {self.age} years old and it's {self.color} and it is cat"
