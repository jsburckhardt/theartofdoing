import random

# Greeting
print("Welcome to the Voter Registration App\n")
# Input from user
name = input("Hello! What is your name: ").strip().title()
print(f"Well {name}, I am thinking of a number between 1 and 20.\n")

# Generate randon number
random_number = random.randint(1,20)
guess = 0
# Setup env
for change_number in range(5):
  guess = int(input("Take a guess: ").strip())
  if guess > random_number:
    print("Your guess is too high.\n")
  elif guess < random_number:
    print("Your guess is too low.\n")
  else:
    break  

if random_number == guess:
  print(f"Good job, {name}! You guessed my number if {change_number + 1} guesses")
else:
  print(f"Game Over. The number I was thinking of was {random_number}")