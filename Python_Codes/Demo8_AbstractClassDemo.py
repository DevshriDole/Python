from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass
class Dog(Animal):
    def sound(self):
        return "Woof!"
class Cat(Animal):
    def sound(self):
        return "Meow!"
# objAnimal = Animal()
objDog = Dog()
print(objDog.sound())
