# Greeting
app = "Event Odd Number Sorter"
print(f"Welcome to the {app} app!")
running = True

while running:
    comma_separated_numbers = (
        input("\nEnter a string of numbers separated by a comma (,): ")
        .lower()
        .strip()
        .split(",")
    )

    # odd and even holder
    odd, even = [], []

    # analyse values and print result summary
    print("\n----- Result Summary -----")
    for number in comma_separated_numbers:
        if int(number) % 2 == 0:
            even.append(int(number))
            print(f"\t{int(number)} is even!")
        else:
            odd.append(int(number))
            print(f"\t{int(number)} is odd!")

    # print odd and even numbers
    print(f"\nThe following {len(even)} numbers are even: ")
    for x in sorted(even):
        print(f"\t{x}")

    print(f"\nThe following {len(odd)} numbers are odd: ")
    for x in sorted(odd):
        print(f"\t{x}")

    # ask if keep running
    running = (
        True if input("\nRun again (y/n): ").strip().lower() == "y" else False
    )

print("Than you for using the program. Good bye")