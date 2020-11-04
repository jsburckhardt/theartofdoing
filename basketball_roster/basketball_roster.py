from random import randrange

# Function to print roster
def print_roster(team):
  print("\n\tYour starting 5 for the upcoming basketball season")
  print(f"\t\t\tPoint Guard:\t\t{team[0]}")
  print(f"\t\t\tShooting Guard:\t\t{team[1]}")
  print(f"\t\t\tSmall Forward:\t\t{team[2]}")
  print(f"\t\t\tPower Forward:\t\t{team[3]}")
  print(f"\t\t\tCenter:\t\t\t{team[4]}\n")

# Welcome message
print("Welcome to the Basketball Roster app\n")

# Define team
team = []
team.append(input("Who is your point guard: ").title())
team.append(input("Who is your shooting guard: ").title())
team.append(input("Who is your small forward: ").title())
team.append(input("Who is your power forward: ").title())
team.append(input("Who is your center: ").title())
print_roster(team)

# Injured player
bad_luck = randrange(5)
injured_player = team.pop(bad_luck)
print(f"Oh no, {injured_player} is injured")
print(f"Your roster only has {len(team)} players")
team.insert(bad_luck,input(f"Who will take {injured_player}'s spot: ").title())
print_roster(team)

# Wishing luck:
print(f"Good luck {team[bad_luck]} you will do great!")
print(f"Your roster now has {len(team)} players.")