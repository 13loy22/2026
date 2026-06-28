import random

# List of possible words
wordslist = [
    "correction",
    "childish",
    "beach",
    "python",
    "assertive",
    "interference",
    "complete",
    "share",
    "credit card",
    "rush",
    "south"
]

# Choose a random word
word = random.choice(wordslist).lower()

# Body parts added after each wrong guess
body_parts = [
    "Head",
    "Body",
    "Left Arm",
    "Right Arm",
    "Left Leg",
    "Right Leg"
]

# Store the letters the player guessed
guessed_letters = []

# Number of wrong guesses
wrong_guesses = 0


# Function to display the word
def show_word(word, guessed_letters):
    for letter in word:
        if letter == " ":
            print(" ", end="")
        elif letter in guessed_letters:
            print(letter, end="")
        else:
            print("*", end="")
    print()


# Function to check if the player guessed the whole word
def word_complete(word, guessed_letters):
    for letter in word:
        if letter != " " and letter not in guessed_letters:
            return False
    return True


print("Welcome to Hangman!")
print()

# Main game loop
while wrong_guesses < 6:

    print("Word:")
    show_word(word, guessed_letters)

    guess = input("Guess one letter: ").lower()

    # Check if only one letter was entered
    if len(guess) != 1:
        print("Please enter only one letter.")
        print()
        continue

    # Check if the letter was already guessed
    if guess in guessed_letters:
        print("You already guessed that letter.")
        print()
        continue

    guessed_letters.append(guess)

    # Correct guess
    if guess in word:
        print("Correct!")
    else:
        print("Wrong guess!")
        print(body_parts[wrong_guesses], "added to the gallows.")
        wrong_guesses += 1

    print("Guessed letters:", guessed_letters)
    print()

    # Check if the player won
    if word_complete(word, guessed_letters):
        print("Congratulations!")
        print("You guessed the word:", word)
        break

# Player loses
if wrong_guesses == 6:
    print("Game Over!")
    print("The word was:", word)