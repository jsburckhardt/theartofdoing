def validate_string(**kwargs):
  message = kwargs.get("message",None)
  item = kwargs.get("item",None)
  size = kwargs.get("size",False)
  value = ''
  retry = 0
  value = input(message)
  while value == '':
    value = input(message)
    retry=retry+1
    if retry >= 3:
      exit(f"ERROR: User didn't provide a {item}")
  retry = 0
  if size:
    while len(value) != 1:
      print(f"Please input just one letter {value}\n")
      value = input(message)
      retry=retry+1
      if retry >= 2:
        exit(f"ERROR: User provide more than 1 letter")
  return value


print("Welcome to the Letter Counter App")
name_validated = validate_string(message="What is your name: ", item="name").capitalize().strip()
print(f"Hello {name_validated}")
print("I will count the number of timesthat a specific letter occurs in a message.")
messsage_validated =  validate_string(message="Please enter a message: ", item="message").lower()
letter_validated = validate_string(message="Which letter would you like to count the occurrences of: ", item="letter", size=True).lower().strip()
count=0
for character in messsage_validated:
  if character == letter_validated:
    count = count + 1
print(f"{name_validated}, the message has {count} {letter_validated}'s in it.")
