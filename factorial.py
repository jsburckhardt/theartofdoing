from math import factorial
# Welcome message
print("Welcome to the Factorial calculator app\n")

# Ask user for number to calculate factorial
number = int(input("What number would you like to number the factorial of? "))

# Creating equation display and computing factorial using loop
equation = '1'
loop_value = 1
for x in range(1,number):
  equation += "*" + str(x+1)
  loop_value *= (x+1)

print(f"{number}! = {equation}\n")

# printing results:
print("Here is the result using the math library:")
print(f"The factorial of {number} is {factorial(number)}!\n")
print("Here is the result using my own algorithm:")
print(f"The factorial of {number} is {loop_value}!\n")

# final message
print(f"It is shown twice that {number}! = {loop_value} (with excitement)")