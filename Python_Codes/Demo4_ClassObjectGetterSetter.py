
class Car:
    # Attributes of the class
    wheels = 4
    make = ""
    model = "" # Model of the car
    year ="" # Year of manufacture

    # Method to set information about the car
    def set_info(self,make1, model1, year1):
        self.make = make1  # Make of the car
        self.model = model1  # Model of the car
        self.year = year1  # Year of manufacture

    # Method to display information about the car
    def display_info(self):
        print(f"Car Information: \nYear of Manufacturing : {self.year} \nMake: {self.make} \nModel: {self.model},\nWheels: {self.wheels}")

if __name__ == '__main__':

    #Setting information by initialising object with setter method
    car1= Car()
    car1.set_info("Toyota", "Corolla", 2020)

    car2 = Car()
    car2.set_info("Honda","Civic",2022)
    
    # Calling method of objects
    car1.display_info()
    car2.display_info()

