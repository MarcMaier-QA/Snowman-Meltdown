from game_logic import play_game


if __name__ == "__main__":
    while True:
        play_game()

        # Ask the player if they want to ply again
        while True:
            again = input("Do you want to play again? (y/n): ").lower()
            if again in ["y", "n"]:
                break # valid input, exit loop
            print("Please enter 'y' for yes or 'n' fo no.")

        if again == "n":
            print("Thanks for playing! Goodbye!")
            break