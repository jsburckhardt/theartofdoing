import random
# Greeting
print("Welcome to a game of Rock, Paper, Scissors\n")
# Input from user
rounds_quantity = int(input("How many rounds would you like to play: ").strip())
player_score, computer_score = 0,0
options = ['rock','paper','scissors']

for round in range(rounds_quantity):
  print(f"\nRound {round+1}")
  print(f"Player: {player_score}\tComputer: {computer_score}")
  player_choice = input("Time to pick ... rock, paper, scissors: ").strip().lower()
  if player_choice not in options:
    print("That's not an option, round goes to the computer")
    computer_score+=1
    break
  computer_choice = random.choices(options).pop()
  print(f"\tComputer: {computer_choice}")
  print(f"\tPlayer: {player_choice}")
  if computer_choice == player_choice:
    print("It is a tie, how boring!")
    print("This round was a tie.")
    continue
  elif (computer_choice == "paper" and player_choice == "rock") or (computer_choice == "rock" and player_choice == "paper"):
    print("Paper covers rock!")
    if computer_choice == 'paper':
      computer_score += 1
      print(f"Computer wins round {round+1}")
    else:
      player_score += 1
      print(f"You win round {round+1}")
    continue
  elif (computer_choice == "paper" and player_choice == "scissors") or (computer_choice == "scissors" and player_choice == "paper"):
    print("Scissors cut paper!")
    if computer_choice == 'scissors':
      computer_score += 1
      print(f"Computer wins round {round+1}")
    else:
      player_score += 1
      print(f"You win round {round+1}")
    continue
  else:
    print("Rock breaks scissors!")
    if computer_choice == 'rock':
      computer_score += 1
      print(f"Computer wins round {round+1}")
    else:
      player_score += 1
      print(f"You win round {round+1}")
  
# results
print("\nFinal Game Results")
print(f"\tRounds Played: {rounds_quantity}")
print(f"\tPlayer Score: {player_score}")
print(f"\tComputer Score: {computer_score}")
if player_score > computer_score:
  print("Winner: YOU! :-)")
elif computer_score > player_score:
  print("Winner: Computer! :-(")
else:
  print("Winner: N/A :?")



