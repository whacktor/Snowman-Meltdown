from game_logic import play_game


def main():
    while True:
        play_game()

        replay = input("Play again? (y/n): ").lower().strip()
        if replay != "y":
            print("Goodbye! 👋")
            break


if __name__ == "__main__":
    main()