import time

# Greeting
app = "Prime Number App"
print(f"Welcome to the {app} app!")
running = True

while running:
    # provide instructions and ask user what he wants to do.
    print("\nEnter 1 to determine if a specific number is prime.")
    print("Enter 2 to determine all prime numbers within a set range.")
    option = int(input("Enter your choice 1 or 2: ").lower().strip())

    # trigger action based on option selected
    if option == 1:
        prime = True
        number_to_validate = int(
            input("\nEnter a number to determine if it is prime or not: ")
        )
        for x in range(2, int(number_to_validate / 2) + 1):
            if number_to_validate % x == 0:
                prime = False
                break
        if prime:
            print(f"{number_to_validate} is prime!")
        else:
            print(f"{number_to_validate} is not prime!")

    elif option == 2:
        # place holder for prime numbers
        prime_list = []
        # ask for limits
        lower_bound = int(
            input("\nEnter the lower bound of your range: ").strip()
        )
        upper_bound = int(
            input("Enter the upper bound of your range: ").strip()
        )
        # start timer
        start_time = time.perf_counter()
        # get prime numbers within limits
        for number_to_validate_in_limit in range(lower_bound, upper_bound + 1):
            if number_to_validate_in_limit == 1:
                continue
            prime = True
            for x in range(2, int(number_to_validate_in_limit / 2) + 1):
                if number_to_validate_in_limit % x == 0:
                    prime = False
                    break
            if prime:
                prime_list.append(number_to_validate_in_limit)
        # finish timer
        end_time = time.perf_counter()

        # present results
        print(
            f"\nCalculations took a total of {end_time-start_time:0.4f} seconds."
        )
        print(
            f"The following numbers between {lower_bound} and {upper_bound} are prime:"
        )
        input("Press enter to continue.")
        for prime in prime_list:
            print(prime)

    else:
        print("That is not a valid option.")
    # ask if keep running
    running = (
        True if input("\nRun again (y/n): ").strip().lower() == "y" else False
    )

print("Than you for using the program. Good bye")