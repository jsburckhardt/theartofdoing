import datetime

# Welcome
print(f"Welcome to the Grocery List App")
print(f"Current Date and Time: {datetime.datetime.now().strftime('%m/%d')}\t{datetime.datetime.now().strftime('%H:%M')}")
print("You currently have Meat and Cheese in your list\n")

# Initialize grocery_list
grocery_list = ["Meat","Cheese"]

# Query user for additional food
for item in range(3):
  grocery_list.append((input("Type of food to add to the grocery list: ").title()))

# Present list
print("\nHere is your grocery list:")
print(str(grocery_list))
grocery_list.sort()
print("Here is your grocery list sorted:")
print(str(grocery_list))

# Simulating grocery shopping 
print("\nSimulating grocery shopping ...\n")
while len(grocery_list) > 2:
  print(f"Current grocery list: {len(grocery_list)} items")
  print(str(grocery_list))
  item_to_remove = input("What food did you just buy: ").title()
  grocery_list.remove(item_to_remove)
  print(f'Removing {item_to_remove} from list ...\n')


# Just two items, ran out of Meat
print(f"Current grocery list: {len(grocery_list)} items")
print(str(grocery_list))
  
print(f"\nSorry, the store is out of {grocery_list.pop()}.")
replace_item = input("What food would you like instead: ").title()
grocery_list.insert(0,replace_item)
print("\nHere is what remains on your grocery list: ")
print(str(grocery_list))