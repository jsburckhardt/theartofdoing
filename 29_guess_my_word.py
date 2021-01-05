import random


def show_a_letter(hint_word, word_to_guess):
    if "-" in hint_word:
        secret_chars = [
            secret_chars
            for secret_chars, char in enumerate(hint_word)
            if char == "-"
        ]
        char_to_disclose = random.choice(secret_chars)
        return (
            hint_word[:char_to_disclose]
            + word_to_guess[char_to_disclose]
            + hint_word[char_to_disclose + 1 :]
        )


# Greeting
app = "Guess My Word"
print(f"Welcome to the {app} app!")
running = True

database = {
    "Sports": ["Soccer", "Football", "Tennis", "Basketball", "Polo"],
    "Fruits": ["Banana", "Strawberry", "Melon", "Mango", "Grape"],
    "Male Names": ["John", "Carl", "Thomas", "Daniel", "Maxwell"],
}


while running:
    # Select random category and word.
    category = random.choice(list(database.keys()))
    word_to_guess = random.choice(database[category])
    word_hint = "-" * len(word_to_guess)

    not_guessed = True
    attempt = 0
    while not_guessed:
        attempt += 1
        print(
            f"Guess a {len(word_to_guess)} letter word from the following category: {category}"
        )
        print(word_hint)
        word_hint = show_a_letter(word_hint, word_to_guess)
        guess = input("\nEnter your guess: ").title().strip()
        if guess == word_to_guess:
            not_guessed = False

    print(f"Correct! You guessed the word in {attempt} guesses.")
    # ask if keep running
    running = (
        True if input("\nRun again (y/n): ").strip().lower() == "y" else False
    )

print("Than you for using the program. Good bye")