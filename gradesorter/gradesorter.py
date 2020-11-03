print("Welcome to the Grade Sorter App")

# Initialize list and ger user input
grades = []
grades.append(int(input("What is your first grade (0-100): ")))
grades.append(int(input("What is your second grade (0-100): ")))
grades.append(int(input("What is your third grade (0-100): ")))
grades.append(int(input("What is your fourth grade (0-100): ")))

print(f"\nYour grades are {str(grades)}")

# Sort the list from highest to lowest
grades.sort(reverse=True)
print(f"\nYour grades from highest to lowest are: {str(grades)}")

# Removing the lawest two grades
print("\nThe lowest two grades will now be dropped:")
print(f"Removed grade: {str(grades.pop())}")
print(f"Removed grade: {str(grades.pop())}")

# Recap remaining grades
print(f"\nRemaining grades are {str(grades)}")
print(f"Nice work! Your highest grade is {str(grades[0])}.")