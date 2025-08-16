import random
from Snowman_Meltdown_Art import STAGES

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]


def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def play_game():
    secret_word = get_random_word()
    print("Welcome to Snowman Meltdown!")
    print("Secret word selected: " + secret_word)  # for testing, later remove this line

    mistakes = 0
    guessed_letters = []

    while True:
        display_game_state(mistakes, secret_word, guessed_letters)

        guess = input("Guess a letter (type 'EXIT' or 0 to quit): ").lower()
        print("You guessed:", guess)

        if guess == "EXIT" or guess == "0":
            print("Bye!")
            break

        mistakes += 1
        guessed_letters.append(guess)

        if mistakes >= len(STAGES):
            print("The snowman melted! GAME OVER!")
            break


def display_game_state(mistakes: int, secret_word: str, guessed_letters: list[str]) -> None:
    """"""
    # 1. ASCII-Art for wrong guesses.
    print(STAGES[mistakes])

    # 2. Secret word with underscore
    display_word = " ".join([letter if letter in guessed_letters else "_" for letter in secret_word])
    print("Word: ", display_word)

    # 3. already guessed letters
    print("Guessed letters:", ' '.join(sorted(guessed_letters)) if guessed_letters else "None")
    print()


if __name__ == "__main__":
    play_game()