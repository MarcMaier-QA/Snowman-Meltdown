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

    attempts = 0
    while True:
        print(STAGES[attempts])
        guess = input("Guess a letter (type 'EXIT' or 0 to quit): ").upper()
        print("You guessed:", guess)

        if guess == "EXIT" or guess == "0":
            print("Bye!")
            break

        # testing attempts for next stage
        attempts += 1
        if attempts >= len(STAGES):
            break


if __name__ == "__main__":
    play_game()