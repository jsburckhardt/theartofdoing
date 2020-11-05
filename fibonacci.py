# Welcome message 
print("Welcome to the Fibonacci Calculator App.\n")

# Ask user for the sequence length
num = int(input("How many digits of the Fibonacci Sequence would you like to computer: "))

# Printing the fibonacci sequence:
print(f"\nThe first {num} numbers of the Fibonacci sequence are: ")
fibo = [0,1]  # init values for calculation
for x in range(2,num+1):
  fibo.append(fibo[x-2]+fibo[x-1])
  print(fibo[x-2]+fibo[x-1])

# Printing Golden Ratio
golden = []
print(f"\nThe corresponding Golden Ratio value are:")
for x in range(len(fibo)-2):  # ignore the last number (can't compare)
  ratio = (fibo[x]+fibo[x+1])/fibo[x+1]
  print(ratio)