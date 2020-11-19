# list price function
users = ['allenj','jsburckhardt','jsarmie4']
quantity_to_ship = 0

def display_price_details():
  print("Current shipping prices are as follows:\n")
  print("Shipping orders 0 to 100:\t\t\t$5.10 each")
  print("Shipping orders 100 to 500:\t\t\t$5.00 each")
  print("Shipping orders 500 to 1000:\t\t\t$4.95 each")
  print("Shipping orders over 1000:\t\t\t$4.80 each")

def print_output_message(quantity,unit_cost):
  print(f"To ship {int(quantity)} items it will cost you ${format(quantity*unit_cost,'.2f')} at ${unit_cost} per item.")


print("Welcome to the Shipping Account Program\n")

# list of users
# receive user input
user = input("Hello, what is your username: ").strip().title()
# validate user in list and display 
if user.lower() not in users:
  print("\nSorry, you do not have an account with us. Goodbye.")
  exit(1)
else:
  print(f"\nHello {user}, welcome back to your account.")
  display_price_details()
  quantity_to_ship = int(input("\nHow many items would you like to ship: "))
  if quantity_to_ship >= 0 and quantity_to_ship < 100:
    print_output_message(quantity_to_ship,5.10)
  elif quantity_to_ship >= 100 and quantity_to_ship < 500:
    print_output_message(quantity_to_ship,5.00)
  elif quantity_to_ship >= 500 and quantity_to_ship < 1000:
    print_output_message(quantity_to_ship,4.95)
  elif quantity_to_ship >= 1000:
    print_output_message(quantity_to_ship,4.80)
  else:
    print("Sorry you can't submit negative quantity")
    exit(1)

if input("\nWould you like to ship this order (y/n): ").strip().lower() == 'y':
  print(f"Okay, Shipping your {quantity_to_ship} items.")
else:
  print("Okay, no order is being placed at this moment")
  