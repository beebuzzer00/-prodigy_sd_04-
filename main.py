import random

# Set the range of the guessing game
lower_bound = 1
upper_bound = 10

# Generate a random number
secret_number = random.randint(lower_bound, upper_bound)

# Initialize variables
attempts = 0
guessed = False

# Start the game loop
while attempts < 5 and not guessed:
    guess = int(input(f"Guess a number between {lower_bound} and {upper_bound}: "))
    attempts += 1

    if guess < secret_number:
        print("Your guess is too low!")
    elif guess > secret_number:
        print("Your guess is too high!")
    else:
        guessed = True
        print(f"Congratulations! You guessed the number in {attempts} attempts!")

if not guessed:
    print(f"Sorry, you ran out of attempts. The number was {secret_number}.")
