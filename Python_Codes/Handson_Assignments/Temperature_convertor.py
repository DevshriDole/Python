
def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

def main():
    temp_val = int(input("Enter the temperature value :"))
    temp_unit = input("Enter the current unit (C for Celsius, F for Fahrenheit): ").strip().upper()
    unit_convert = input("Enter the target unit (C for Celsius, F for Fahrenheit): ").strip().upper()

    if temp_unit == 'C' and unit_convert == 'F':
        converted = celsius_to_fahrenheit(temp_val)
        print(f"{temp_val}°C is {converted}°F")
    elif temp_unit == 'F' and unit_convert == 'C':
        converted = fahrenheit_to_celsius(temp_val)
        print(f"{temp_val}°F is {converted}°C")
    else:
        print("Invalid unit conversion. Please use 'C' for Celsius and 'F' for Fahrenheit.")


if __name__ == "__main__":
    main()



