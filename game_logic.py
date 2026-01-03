
import random
from ascii_art import STAGES, WORDS


def get_random_word():
    """Selects a random word from the list."""
    return random.choice(WORDS)


def display_game_state(mistakes, secret_word, guessed_letters):
    """Displays current game state (snowman stage + word progress)."""
    print(STAGES[mistakes])

    display_word = ""
    for letter in secret_word:
        display_word += (letter + " ") if letter in guessed_letters else "_ "

    print("Word:", display_word.strip())
    print()


def play_game():
    secret_word = get_random_word()
    guessed_letters = set()
    mistakes = 0
    max_mistakes = len(STAGES) - 1

    print("Welcome to Snowman Meltdown!")
    print("Try to save the snowman by guessing the word!")

    while True:
        display_game_state(mistakes, secret_word, guessed_letters)

        # Win condition
        if all(letter in guessed_letters for letter in secret_word):
            print("🎉 You saved the snowman! The word was:", secret_word)
            return

        # Lose condition
        if mistakes >= max_mistakes:
            print("💧 Oh no, the snowman melted completely!")
            print("The word was:", secret_word)
            return

        guess = input("Guess a letter: ").lower().strip()

        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter (a-z).")
            continue

        # Already guessed
        if guess in guessed_letters:
            print("You already guessed that letter. Try another one.")
            continue

        # Store guess
        guessed_letters.add(guess)

        # Check guess
        if guess in secret_word:
            print("✅ Correct guess!")
        else:
            print("❌ Wrong guess!")
            mistakes += 1