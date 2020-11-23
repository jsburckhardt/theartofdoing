print("Welcome to the Voter Registration App\n")
name = input("Please enter your name: ").strip().title()
age = int(input("Please enter your age: ").strip())
party_ismajor = False
parties = ['republican','democratic','independent','libertarian','green']

if age > 17:
  print(f"\nCongratulations {name}! You are old enough to register to vote\n")
  print("Here is a list of political parties to join.")
  for party in parties:
    print(f"\t\t- {party.title()}")    
  selected_party = input("\nWhat party would you like to join: ").strip().lower()
  if selected_party not in parties:
    print("Wrong option!")
    exit(1)
  if selected_party == "republican" or selected_party == "democratic":
    party_ismajor = True
  if party_ismajor:
    print(f"\nCongratulations {name}! You have joined the {selected_party.title()} party!\nThat is a major party!")
  else:
    print(f"\nCongratulations {name}! You have joined the {selected_party.title()} party!\nThat is not a major party!")
else:
  print("You are not old enough to register to vote.")