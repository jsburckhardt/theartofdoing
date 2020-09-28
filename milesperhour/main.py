print("Welcome to the MPH to MPS Conversion App\n")
speed_mph = float(input("What is your speed in miles per hour: "))
speed_mps = round((speed_mph * 1609.344)/3600,2)

print(f"Your speed in meters per second is: {speed_mps}")
