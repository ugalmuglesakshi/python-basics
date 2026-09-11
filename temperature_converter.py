temperature = float(input("Enter temperature: "))
unit = input("Enter unit (C/F): ").upper()

if unit == "C":
    fahrenheit = (temperature * 9 / 5) + 32
    print("Temperature in Fahrenheit:", fahrenheit, "°F")

elif unit == "F":
    celsius = (temperature - 32) * 5 / 9
    print("Temperature in Celsius:", celsius, "°C")

else:
    print("Invalid unit. Please enter C or F.")