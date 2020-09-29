print("Welcome to the Temperature Conversion App App\n")
degrees_f = round(float(input("What is the given temperature in degrees Fahrenheit: ")),4)
degrees_c = round((degrees_f-32)*(5/9),4)
degrees_k = round((degrees_f+459.67)*(5/9),4)

print(f"Degrees Fahrenheit:\t{degrees_f}")
print(f"Degrees Celsius:\t{degrees_c}")
print(f"Degrees Kelvin: \t{degrees_k}")
