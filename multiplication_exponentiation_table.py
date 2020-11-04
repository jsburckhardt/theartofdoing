import string

def multiplication_table(number_to_play):
  print(f"\nMultiplication Table For {number_to_play}\n")
  for x in range(9):
    print(f"\t\t{float(x+1)} * {number_to_play} = {int(x+1)*number_to_play}")


def exponent_table(number_to_play):
  print(f"\nExponent Table For {number_to_play}\n")
  for x in range(9):
    print(f"\t\t{number_to_play} ** {int(x+1)} = {number_to_play ** int(x+1)}")

def bye_message(user_name):
  first_part = user_name + ' Math'
  second_part = "is cool!"
  print(f"\n{string.capwords(first_part)} {second_part.lower()}")
  print(f"\t\t{first_part.lower()} {second_part.lower()}")
  print(f"\t\t\t\t{string.capwords(first_part)} {string.capwords(second_part)}")
  print(f"\t\t\t\t\t\t{first_part.upper()} {second_part.upper()}")
  


print("Welcome to the Multiplication/Exponent Table app")
user_name = input("Hello, what is your name: ").strip().capitalize()
number_to_play = float(input("What number would you like to work with: "))
multiplication_table(number_to_play)
exponent_table(number_to_play)
bye_message(user_name)
