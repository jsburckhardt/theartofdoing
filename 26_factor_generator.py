# Greeting
app = "Factor Generator"
print(f"Welcome to the {app} app!")
running = True

while running:
    number_to_analyse = int(
        input("\nEnter a number to determine all factors of that number: ")
        .lower()
        .strip()
    )

    # place holder for factors
    factors = []

    # find all factors for the number to analyse
    for x in range(1, int(number_to_analyse / 2)):
        if number_to_analyse % x == 0:
            factors.append(x)
    # include itself
    factors.append(number_to_analyse)
    # print factors:
    print(f"\nFactors of {number_to_analyse} are:")
    for x in factors:
        print(x)

    # print summary:
    print("\nIn summary:")

    middle = (
        int(len(factors) / 2)
        if len(factors) % 2 == 0
        else int(len(factors) / 2) + 1
    )

    for x in range(middle):
        print(f"{factors[x]} * {factors[-1-x]} = {number_to_analyse}")

    running = (
        True if input("\nRun again (y/n): ").strip().lower() == "y" else False
    )

print("Than you for using the program. Have a great day")