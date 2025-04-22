def convert_inches(value, target_unit):
    if target_unit.lower() == "feet":
        return value / 12
    elif target_unit.lower() == "meters":
        return value * 0.0254
    elif target_unit.lower() == "centimeters":
        return value * 2.54
    else:
        return None

while True:
    try:
        # Input value and unit
        input_value = float(input("Enter the value in inches: "))
        input_unit = input("Enter the unit of the input value (should be 'inches'): ").lower()

        # Only allow inches as input
        if input_unit != "inches":
            print("Sorry, this program only accepts inches as the input unit.")
            continue

        # Target unit selection
        target_unit = input("Enter the target unit (feet, meters, centimeters): ").lower()

        # Conversion
        result = convert_inches(input_value, target_unit)
        if result is not None:
            print(f"{input_value} inches is equal to {result:.2f} {target_unit}.")
        else:
            print("Invalid target unit entered.")

        # Repeat?
        repeat = input("Do you want to convert another value? (Yes/No): ").strip().lower()
        if repeat != 'yes':
            print("Exiting the converter. Goodbye!")
            break
    except ValueError:
        print("Invalid input. Please enter a numeric value for the measurement.")