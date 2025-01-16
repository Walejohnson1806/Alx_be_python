FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5


def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR


def convert_to_fahrenheit(celsius):
    return celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32


prompt1 = int(input("Enter the temperature to convert: "))
prompt2 = input("Is this temperature in Celsius or Fahrenheit? (C/F):").strip().upper()

if prompt2 == "C":
    print(f"{prompt1}°C is {convert_to_fahrenheit(prompt1)}°F")
elif prompt2 == "F":
    print(f"{prompt1}°F is {convert_to_celsius(prompt1)}°C")

else:
    print("Invalid temperature. Please enter a numeric value.")