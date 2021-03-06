from collections import Counter
import string

# Greeting
app = "Frequency Analysis"
print(f"Welcome to the {app} app!")

# go through 2 use cases
for phrase_number in range(2):
    # acceptable lowecase values to store totals
    result_analysis = dict.fromkeys(string.ascii_lowercase, 0)
    total = 0
    ordered_letters = [{"_": 0}]
    # Get user data
    sentence = list(
        input(
            "\nEnter a word or phrase to count the occurrence of each letter: "
        )
        .strip()
        .lower()
    )

    for char in sentence:
        if char.isalnum():
            result_analysis[char] = result_analysis[char] + 1
            total += 1

    print(
        f"\nHere is the frequency analysis from key phrase {phrase_number+1}\n"
    )
    print("\t\tLetter\t\tOccurrence\t\tPercentage")
    ordered_items = [{"-": 0}]
    for character, value in sorted(result_analysis.items()):
        if result_analysis[character] != 0:
            print(
                f"\t\t{character}\t\t{value}\t\t\t{round(value*100/total,2)}%"
            )
            for x in range(len(ordered_items)):
                if value > list(ordered_items[x].values())[0]:
                    ordered_items.insert(x, {character: value})
                    break
    print("\nLetters ordered from highest occurrence to lowest:")
    for sorted_key in ordered_items[:-1]:
        print(list(sorted_key.keys())[0], end="")
    print("")
