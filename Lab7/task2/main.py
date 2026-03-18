from dog import Dog
from cat import Cat
    
if __name__ == "__main__":
    dog1 = Dog("Buddy", age=3, color="golden", breed="Labrador")
    dog2 = Dog("Rex", age=5, color="black", breed="German Shepherd", sound="Bark")
    cat1 = Cat("Whiskers", age=4, color="white", is_indoor=True)
    cat2 = Cat("Shadow", age=2, color="black", is_indoor=False, sound="hiss")
 
    animals = [dog1, dog2, cat1, cat2]
 
    print("=" * 55)
    print("          ALL ANIMALS — __str__")
    print("=" * 55)
    for animal in animals:
        print(animal)
 
    print("\n" + "=" * 55)
    print("          POLYMORPHISM — make_sound()")
    print("=" * 55)
    for animal in animals:
        print(animal.make_sound())
 
    print("\n" + "=" * 55)
    print("          UNIQUE METHODS")
    print("=" * 55)
    for animal in animals:
        if isinstance(animal, Dog):
            print(animal.fetch("ball"))
        elif isinstance(animal, Cat):
            print(animal.where_isit())
 
    print("\n" + "=" * 55)
    print("          BIRTHDAY METHOD (inherited)")
    print("=" * 55)
    for animal in animals:
        print(animal.birthday())
