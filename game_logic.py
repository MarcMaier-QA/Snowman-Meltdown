import random
from ascii_art import STAGES

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]

def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def display_game_state(mistakes: int, secret_word: str, guessed_letters: list[str]) -> None:
    """
    Displays the current state of the Snowman Meltdown game.

    Shows the ASCII-art representation of the snowman based on the number of mistakes,
    the secret word with underscores for letters that have not been guessed yet,
    and the list of letters that have already been guessed.

    :param mistakes: The number of incorrect guesses so far.
    :param secret_word: The word the player is trying to guess.
    :param guessed_letters: The letters that the player has guessed so far.

    :return: None
    """
    # 1. ASCII-Art for wrong guesses.
    print(STAGES[mistakes])

    # 2. Secret word with underscore
    display_word = " ".join([letter if letter in guessed_letters else "_" for letter in secret_word])
    print("Word: ", display_word)

    # 3. already guessed letters
    print("Guessed letters:", ' '.join(sorted(guessed_letters)) if guessed_letters else "None")
    print()


def play_game():
    """
    Starts and runs the snowman Meltdown game.

    The player tries to guess a randomly selected  secret word one letter at a time.
    Displays the current game state with ASCII-art, tracks guessed letters and mistakes,
    and ends the game when the player either guesses the word or the snowman melts.

    The player can type 'EXIT' or '0' to quit the game at any time.

    :return: None
    """
    secret_word = get_random_word()
    print("Welcome to Snowman Meltdown!")
    print("Secret word selected: " + secret_word)  # for testing, later remove this line

    mistakes = 0
    guessed_letters = []

    while True:
        display_game_state(mistakes, secret_word, guessed_letters)

        guess = input("Guess a letter (type 'EXIT' or 0 to quit): ").lower()
        print("You guessed:", guess)

        # Check if the player wants to quit
        if guess == "exit" or guess == "0":
            print("Bye!")
            break

        # Input Validation: only allows a single alphabetic character
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter (a-z).")
            continue

        # CHeck if the letter was already guessed
        if guess in guessed_letters:
            print(f"You already guessed the letter '{guess}'!")
            continue

        # Add the guessed letter to the list of guessed letters
        guessed_letters.append(guess)

        # Increment mistakes if the guess is wrong
        if guess not in secret_word:
            mistakes += 1
            print(f"{guess} wrong guess!")

        # Check if the snowman has melted (game over)
        if mistakes >= len(STAGES):
            print("The snowman melted! GAME OVER!")
            break

        # Checkt if all letters have been guessed (player wins)
        if all(letter in guessed_letters for letter in secret_word):
            print("Congratulations! You guessed the word:", secret_word)
            break
