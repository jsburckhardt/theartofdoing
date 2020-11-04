from cmath import sqrt
# Welcome message
print("Welcome to the Quadratic Solver App.")

# Summary of app
print("""
A quadratic equation is of the form ax^2 + bx + c = 0
Your solutions can be real or complex numbers.
A comples number has two parts: a + bj
Where a is the real portion and the bj is the imaginary portion.
""")

# Ask the number of equations to solve
quantity_of_equations = int(input("How many equations would you lie to solve today: "))

# solve equations
for equation in range(quantity_of_equations):
  print(f"\nSolving equation #{equation + 1}")
  print("-"*100 + "\n")
  coefficient_a = float(input("Please enter your value of a (coefficient of x^2): "))
  coefficient_b = float(input("Please enter your value of b (coefficient of x): "))
  coefficient_c = float(input("Please enter your value of c (coefficient): "))
  print(f"\nThe solutions to {coefficient_a}x^2 + {coefficient_b}x + {coefficient_c} are:\n")

  print(f"\tx1 = {complex((-coefficient_b + sqrt(coefficient_b**2 - (4 * coefficient_a * coefficient_c)))/(2 * coefficient_a))}")
  print(f"\tx2 = {complex((-coefficient_b - sqrt(coefficient_b**2 - (4 * coefficient_a * coefficient_c)))/(2 * coefficient_a))}")
