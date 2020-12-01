import random

# Greeting
app = "Thesaurus"
print(f"Welcome to the {app} app!\n")

print("Choose a word from the thesaurus and I will give you a synonym.\n")

# thesaurus
thesaurus = {
  "hot": ["roasting", "searing", "flaming", "parching", "blistering"],
  "cold": ["chilly", "cool", "freezing", "icy", "snowy"],
  "happy": ["contented", "content", "cheerful", "cheery", "merry"],
  "sad": ["unhappy", "sorrowful", "dejected", "regretful", "depressed"]
}

print("Here are the words in the thesaurus:")
for word in thesaurus.keys():
  print(f"\t- {word}")

# Input from user and validation
word_to_look = input("\nWhat word would you like a synonym for: ").strip().lower()
if word_to_look not in thesaurus.keys():
  print('Wrong word')
  exit(1)

random_synonym = random.choice(thesaurus[word_to_look])
print(f'A synonym for {word_to_look} is {random_synonym}.\n')

# print thesaurus?
print_thesaurus = True if input("Would you like to see the whole thesaurus (yes/no): ").strip().lower() == 'yes' else False

if print_thesaurus:
  for word in thesaurus.keys():
    print(f"\n{word.title()} synonyms are: ")
    for synonym in thesaurus[word]:
      print(f"\t- {synonym}")
else:
  print("\nI hope you enjoyed the program. Thank you!")