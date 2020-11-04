# Function to print details
def print_favorite_teachers_details(teachers_details):
  # Generate copy of list
  print(f"\nYour favorite teachers ranked are: {teachers_details}")
  print(f"Your favorite teachers alphabetically order are: {sorted(teachers_details)}")
  print(f"Your favorite teachers in reverse alphabetically order are: {sorted(teachers_details,reverse=True)}\n")
  print(f"Your top two teachers are: {teachers_details[:2]}.")
  print(f"Your next two favorite teachers are: {teachers_details[2:4]}.")
  print(f"Your last favorite teacher is: {teachers_details[-1]}.")
  print(f"You have a total of {len(teachers_details)} favorite teachers.\n")


print("Welcome to the Favorite Teachers app\n")

# read user input and store teachers
teachers = []
quantity_of_teachers = 4
while len(teachers) < quantity_of_teachers:
  teachers.append(input(f"Who is your {len(teachers)+1} favorite teacher: ").title())

# printing details
print_favorite_teachers_details(teachers)

# Include new favorite teacher and print details
teachers.insert(0,input(f"Oops, {teachers[0]} is no longer your first favorite teacher. Who is your new FAVORITE teacher: ").title())
print_favorite_teachers_details(teachers)

# Remove non favorite teacher and print details
teachers.remove(input(f"You've decided you no longer like a teacher. Which teacher would you like to remove from your list: ").title())
print_favorite_teachers_details(teachers)