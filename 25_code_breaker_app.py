from collections import Counter
import string

# Greeting
app = "Code Breaker"
print(f"Welcome to the {app} app!")
pass_phrase_code = []

# Create codes for encoding/decoding a message
for phrase_number in range(2):
    # acceptable lowecase values to store totals
    result_analysis = dict.fromkeys(string.ascii_lowercase, 0)
    total = 0
    ordered_letters = [{"_": 0}]
    # Get user data
    pass_phrases = [
        """To Sherlock Holmes she is always THE woman. I have seldom heard him mention her under any other name. In his eyes she eclipses and predominates the whole of her sex. It was not that he felt any emotion akin to love for Irene Adler. All emotions, and that one particularly, were abhorrent to his cold, precise but admirably balanced mind. He was, I take it, the most perfect reasoning and observing machine that the world has seen, but as a lover he would have placed himself in a false position. He never spoke of the softer passions, save with a gibe and a sneer. They were admirable things for the observer--excellent for drawing the veil from men's motives and actions. But for the trained reasoner to admit such intrusions into his own delicate and finely adjusted temperament was to introduce a distracting factor which might throw a doubt upon all his mental results. Grit in a sensitive instrument, or a crack in one of his own high-power lenses, would not be more disturbing than a strong emotion in a nature such as his. And yet there was but one woman to him, and that woman was the late Irene Adler, of dubious and questionable memory. I had seen little of Holmes lately. My marriage had drifted us away from each other. My own complete happiness, and the home-centred interests which rise up around the man who first finds himself master of his own establishment, were sufficient to absorb all my attention, while Holmes, who loathed every form of society with his whole Bohemian soul, remained in our lodgings in Baker Street, buried among his old books, and alternatizng from week to week between cocaine and ambition, the drowsiness of the drug, and the fierce energy of his own keen nature. He was still, as ever, deeply attracted by the study of crime, and occupied his immense faculties and extraordinary powers of observation in following out those clues, and clearing up those mysteries which had been abandoned as hopeless by the official police. From time to time I heard some vague account of his doings: of his summons to Odessa in the case of the Trepoff murder, of his clearing up of the singular tragedy of the Atkinson brothers at Trincomalee, and finally of the mission which he had accomplished so delicately and successfully for the reigning family of Holland.""",
        """The Lord St. Simon marriage, and its curious termination, have long ceased to be a subject of interest in those exalted circles in which the unfortunate bridegroom moves. Fresh scandals have eclipsed it, and their more piquant details have drawn the gossips away from this four-year-old drama. As I have reason to believe, however, that the full facts have never been revealed to the general public, and as my friend Sherlock Holmes had a considerable share in clearing the matter up, I feel that no memoir of him would be complete without some little sketch of this remarkable episode. It was a few weeks before my own marriage, during the days when I was still sharing rooms with Holmes in Baker Street, that he came home from an afternoon stroll to find a letter on the table waiting for him. I had remained indoors all day, for the weather had taken a sudden turn to rain, with high autumnal winds, and the Jezail bullet which I had brought back in one of my limbs as a relic of my Afghan campaign throbbed with dull persistence.""",
    ]
    sentence = list(pass_phrases[phrase_number].strip().lower())

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
    # safe the code
    pass_phrase_code.append(ordered_items[:-1])

action = (
    input("\nWould you like to encode or decode a message: ").lower().strip()
)

if action == "encode":
    # encoding the message by finding the letter in the first pass_phrase_code
    # and replacing it with the same letter possition from the second message
    encoded_result = ""
    phrase_to_encode = (
        input("What is the phrase: ").strip().lower()
    )  # ask user for the phrase
    for char in phrase_to_encode:
        for index, code_letter in enumerate(pass_phrase_code[0]):
            if char == list(code_letter.keys())[0]:
                encoded_result = (
                    encoded_result + list(pass_phrase_code[1][index].keys())[0]
                )
    print(f"Encoded result: {encoded_result}")

elif action == "decode":
    # decondign the message by looking the letters in the second pass_phrase_code
    # and using the first one as source.
    decoded_result = ""
    phrase_to_decode = (
        input("What is the encoded message: ").strip().lower()
    )  # ask user for the message
    for char in phrase_to_decode:
        for index, code_letter in enumerate(pass_phrase_code[1]):
            if char == list(code_letter.keys())[0]:
                decoded_result = (
                    decoded_result + list(pass_phrase_code[0][index].keys())[0]
                )
    print(f"Encoded result: {decoded_result}")
else:
    print("Wrong option")