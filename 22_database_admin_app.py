# Greeting
app = "Database Admin"
print(f"Welcome to the {app} app!\n")

database = {
  "mooman74": "alskes145",
  "meramo1986": "kehns010101",
  "nickyd": "world1star",
  "george2": "boo3oha",
  "admin00": "admin1234",
}

# input from user
username_input = input("Enter your username: ").strip().lower()

if username_input in database.keys():
  password_input = input("Enter your password: ").strip()
  if password_input == database[username_input]:
    print(f"\nHello {username_input}! You are logged in!")
    if username_input == 'admin00':
      for user, value in database.items():
        print(f"Username: {user}\t\tPassword: {value}")
    else:
      change_password = input("Would you like to change your password (yes/no): ").strip().lower()
      if change_password == 'yes':
        new_password = input("What would you like your new password to be: ").strip()
        if len(new_password) > 8:
          database[username_input] = new_password
        else:
          print(f"{new_password} not the minimum eight characters.")
      print(f"\n{username_input} your password is {database[username_input]}")    
  else:
    print("wrong option")
else:
 print("User not in database")
