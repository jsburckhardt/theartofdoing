# Function to print details
def give_details(name_of_list, list_to_analyze):
  print(f"The variables {name_of_list} is a {type(list_to_analyze)}.")
  print(f"It contains the elements: {list_to_analyze}")
  print(f"The element {list_to_analyze[0]} is a {type(list_to_analyze[0])}.\n")

# Defining lists
num_strings = ['15','100','55','42']
num_ints = [15,100,55,42]
num_floats = [2.2,5.0,1.245,0.142857]
num_lists = [[1,2,3],[4,5,6,],[7,8,9]]

# Printing summary table
print("\t\tSummary Table\n")
give_details("num_strings",num_strings)
give_details("num_ints",num_ints)
give_details("num_floats",num_floats)
give_details("num_lists",num_lists)

# Sorting num_strings and num_ints
num_strings.sort()
num_ints.sort()
print("Now sorting num_strings and num_ints ...")
print(f"Sorted num_strings: {str(num_strings)}")
print(f"Sorted num_ints: {str(num_ints)}")

print("Strings are sorted alphabetically while integers are sorted numerically!")