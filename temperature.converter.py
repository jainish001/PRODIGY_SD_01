                                                                           ##TASK - 1
def convert_from_celsius(c):
    f = (c * 9/5) + 32
    k = c + 273.15
    return f, k

def convert_from_fahrenheit(f):
    c = (f - 32) * 5/9
    k = c + 273.15
    return c, k

def convert_from_kelvin(k):
    c = k - 273.15
    f = (c * 9/5) + 32
    return c, f

print('''Temperature Converter
       1. Celsius
       2. Fahrenheit
       3. Kelvin''')

choice = input("Enter your choice (1/2/3): ")

if choice == '1':
    c = float(input("Enter temperature in Celsius: "))
    f, k = convert_from_celsius(c)
    print(f"Fahrenheit: {f:.2f}°F")
    print(f"Kelvin: {k:.2f}K")

elif choice == '2':
    f = float(input("Enter temperature in Fahrenheit: "))
    c, k = convert_from_fahrenheit(f)
    print(f"Celsius: {c:.2f}°C")
    print(f"Kelvin: {k:.2f}K")

elif choice == '3':
    k = float(input("Enter temperature in Kelvin: "))
    c, f = convert_from_kelvin(k)
    print(f"Celsius: {c:.2f}°C")
    print(f"Fahrenheit: {f:.2f}°F")

else:
    print("Invalid choice. Please enter 1, 2, or 3.")
