
class Car:
    # Attributes of the class
    wheels = 4
    make = ""
    model = "" # Model of the car
    year ="" # Year of manufacture

    #The __init__ method is called the constructor and initializes object attributes
    def __init__(self, make1, model1, year1):
        # Attributes of the class
        self.make = make1   # Make of the car
        self.model = model1 # Model of the car
        self.year = year1   # Year of manufacture
        #Car.wheels = 6

    # Method to display information about the car
    def display_info(self):
        print(f"Car Information: \nYear of Manufacturing : {self.year} \nMake: {self.make} \nModel: {self.model},\nWheels: {self.wheels}")

if __name__ == '__main__':

    car1 = Car("Toyota", "Corolla", 2020)
    car2 = Car("Honda","Civic",2022)

    #Public variable
    car1.wheels = 3

    # Calling the method of the objects
    car1.display_info()  # Output: Car Information: 2020 Toyota Corolla
    car2.display_info()  # Output: Car Information: 2022 Honda Civic
