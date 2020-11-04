# print slices function
def print_slices(num_list,base,start,stop):
  print(f"{base.title()} values from {start} to {stop}")
  for number in num_list[start-1:stop]:
    print(number)

# welcome message
print("Welcome to the Binary/Hexadecimal Converter App\n")
# asking user for limit
upper_limit = int(input("Compute binary and hexadecimal values up to the following decimal number: "))

# Create lists for each base
print("Generating lists ... Complete!\n")
decimal, binary, hexadecimal = [],[],[]
for number in range(upper_limit):
  decimal.append(number+1)
  binary.append(bin(number+1))
  hexadecimal.append(hex(number+1))

# creating slices and getting input from user
print("Using slices, we will now show a portion of each list")
start_num = int(input("What decimal number would you like to start at: "))
stop_num = int(input("What decimal number would you like to stop at: "))

print_slices(decimal, "decimal", start_num, stop_num)
print_slices(binary, "Binary", start_num, stop_num)
print_slices(hexadecimal, "Hexadecimal", start_num, stop_num)

# Print all table after user input
input(f"\nPress ENTER to see all the values from 1 to {upper_limit}.")
print("Decimal-----Binary-----Hexadecimal")
print('-'*100)
for number in range(upper_limit):
  print(f"{number+1}-----{bin(number+1)}-----{hex(number+1)}")
