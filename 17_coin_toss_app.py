import random

print("Welcome to the Shipping Account Program\n")

print("I will flip a coin a set number of times.")
flip_times = int(input("How many times would you like me to flip the coin: "))

results = []
flip_options = ["TAILS","HEADS"]
tails_total, heads_total = 0,0
details = True if input("Would you like to see the result of each flip (y/n): ").lower().strip() == 'y' else False
if details:
  print("\nFLIPPING!!!\n")
for _ in range(flip_times):
  if random.choice(flip_options) == 'TAILS':
    tails_total += 1
    if details:
        print('TAILS')
  else:
    heads_total += 1
    if details:
      print('HEADS')
  if tails_total == heads_total and details:
    print(f'At {tails_total + heads_total} flips, the number of heads and tails were equal at {tails_total}')

print(f"\nResults Of Flipping A Coin {flip_times}:\n")
print("SIDE\t\tCount\t\tPercentage")
print(f"Heads\t\t{heads_total}/{flip_times}\t\t{format((heads_total/flip_times) * 100,'.1f')}")
print(f"Tails\t\t{tails_total}/{flip_times}\t\t{format((tails_total/flip_times) * 100,'.1f')}")

      