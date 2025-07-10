# Base class
class Animal:
    def __init__(self, name):
        self.name = name  # Encapsulation

    def speak(self):  # Polymorphism
        return f"{self.name} makes a sound"

# Derived class (Inheritance)
class Dog(Animal):
    def speak(self):  # Polymorphism
        return f"{self.name} says Woof!"

class Cat(Animal):
    def speak(self):  # Polymorphism
        return f"{self.name} says Meow!"

# Another class to show composition
class Zoo:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):  # Encapsulation
        self.animals.append(animal)

    def show_sounds(self):
        for animal in self.animals:
            print(animal.speak())

# Creating objects
dog1 = Dog("Buddy")
cat1 = Cat("Whiskers")

# Using Zoo class
zoo = Zoo()
zoo.add_animal(dog1)
zoo.add_animal(cat1)

# Output sounds
zoo.show_sounds()
