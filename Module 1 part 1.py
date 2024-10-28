#changes celsius to fahrenheit
def celsius_to_fahrenheit(C):
    return (9/5) * C + 32

#ask user to enter a temperature in celsius
#when printing an error occurs because c is not a float
C = float(input("Enter a temperature in Celsius: "))

#assigns formula to a function for easier print
F = celsius_to_fahrenheit(C)

#prints conversion
print (f"{C}°C is {F}°F")
