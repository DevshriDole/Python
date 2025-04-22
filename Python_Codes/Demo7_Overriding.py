class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

    # def speak1(self):
    #     print("Dog barks")

class Cat(Animal):
    def speak(self):
        print("Cat meows")

def make_animal_speak(animal_obj):
    animal_obj.speak()

# Usage
dog_obj = Dog()
cat_obj = Cat()
make_animal_speak(dog_obj)  # Output: Dog barks
make_animal_speak(cat_obj)  # Output: Cat meows
