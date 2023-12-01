def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

def temperature_conversion():
    print("Welcome to the Temperature Conversion Program!")
    print("Available temperature units: Celsius, Fahrenheit, Kelvin")
    original_unit = input("Enter the original temperature unit (Celsius, Fahrenheit, Kelvin): ").lower()

    if original_unit not in ['celsius', 'fahrenheit', 'kelvin']:
        print("Invalid input. Please enter a valid temperature unit.")
        return

    temperature = float(input(f"Enter the temperature in {original_unit}: "))

    if original_unit == 'celsius':
        fahrenheit = celsius_to_fahrenheit(temperature)
        kelvin = celsius_to_kelvin(temperature)
        print(f"{temperature}°C is equal to {fahrenheit}°F and {kelvin}K.")
    elif original_unit == 'fahrenheit':
        celsius = fahrenheit_to_celsius(temperature)
        kelvin = fahrenheit_to_kelvin(temperature)
        print(f"{temperature}°F is equal to {celsius}°C and {kelvin}K.")
    else:
        celsius = kelvin_to_celsius(temperature)
        fahrenheit = kelvin_to_fahrenheit(temperature)
        print(f"{temperature}K is equal to {celsius}°C and {fahrenheit}°F.")

temperature_conversion()
