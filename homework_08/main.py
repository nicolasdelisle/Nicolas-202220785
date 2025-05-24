import temperature
def main():
    try:
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))

        converted_to_fahrenheit = temperature.celsius_to_fahrenheit(celsius)
        converted_to_celsius = temperature.fahrenheit_to_celsius(fahrenheit)

        print(f"{celsius:.2f}°C is {converted_to_fahrenheit:.2f}°F")
        print(f"{fahrenheit:.2f}°F is {converted_to_celsius:.2f}°C")
        
    except ValueError:
        print("Please enter valid numeric values.")

main()