# Base class (Superclass)
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound"

# Derived class (Subclass) inheriting from Animal
class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

# Another derived class (Subclass) inheriting from Animal
class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

# Using the classes
dog = Dog("Bruno")
cat = Cat("Lucy")

print(dog.speak())
print(cat.speak())
