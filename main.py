from game_logic import play_game


def main():
    """
    Start the game and handle replay logic.
    """
    while True:
        play_game()

        # Ask the player if they want to ply again
        while True:
            again = input("Do you want to play again? (y/n): ").lower()
            if again in ["y", "n"]:
                break  # valid input, exit loop
            print("Please enter 'y' for yes or 'n' for no.")

        if again == "n":
            print("Thanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()
