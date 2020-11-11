# Welcome message 
print("Welcome to the Fibonacci Calculator App.\n")

# Ask user for the sequence length
num = int(input("How many digits of the Fibonacci Sequence would you like to computer: "))

# generate fibonacci sequence:
fibo = [1,1]  # init values for calculation
for x in range(num-2):
  fibo.append(fibo[x]+fibo[x+1])

# generating Golden Ratio
golden = []
for x in range(num-1):  # ignore the last number (can't compare)
  golden.append(fibo[x+1]/fibo[x])

print(f"\nThe first {num} numbers of the Fibonacci sequence are: ")
for x in range(len(fibo)):
  print(fibo[x])

print(f"\nThe corresponding Golden Ratio value are:")
for x in range(len(golden)):
  print(golden[x])