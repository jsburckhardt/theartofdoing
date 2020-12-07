# Greeting
app = "Yes or No Issues Polling"
print(f"Welcome to the {app} app!\n")

# Get user data
issue = input(
    "What is the yes or no issue you will be voting on today? ").strip().capitalize()
number_of_voters = int(
    input("What is the number of voters you will allow on the issue? ").strip())
results_password = input("Enter a password for polling results: ")

results = {}

for _ in range(number_of_voters):
    voter_name = input("\nEnter your full name: ").strip().title()
    if voter_name in results.keys():
        print("Sorry, it seems taht someone with that name has already voted.")
    else:
        print(f'Here is our issue: {issue}')
        vote = input("What do you think... yes or no").strip().lower()
        results[voter_name] = vote
        print(
            f"Thank you {voter_name}! Your vote of {vote} has been recorded.")

print(f"\nThe following {len(results)} voted:")
for voter_name in results.keys():
    print(voter_name)

votes_yes = list(results.values()).count('yes')
votes_no = list(results.values()).count('no')

print(f"\nOn the following issue: {issue}")
if votes_yes > votes_no:
    print(f"Yes wins! {votes_yes} votes to {votes_no}.")
elif votes_yes < votes_no:
    print(f"No wins! {votes_no} votes to {votes_yes}.")
else:
    print(f"No wins! {votes_no} votes to {votes_yes}.")
