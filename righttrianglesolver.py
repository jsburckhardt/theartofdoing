import math

print("Welcome to the Triangle Solver App\n")

first_leg =  round(float(input("What is the first leg of the triangle: ")),3)
second_leg =  round(float(input("What is the second leg of the triangle: ")),3)

hypotenouse = round(math.sqrt(math.pow(first_leg,2)+math.pow(second_leg,2)),3)
area = round((first_leg * second_leg)/2,3)

print(f"\nFor a triangle with legs of {first_leg} and {second_leg} the hypotenuse is {hypotenouse}")
print(f"For a triangle with legs of {first_leg} and {second_leg} the area is {area}")

