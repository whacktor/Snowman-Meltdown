
import random
from ascii_art import STAGES

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]


def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def display_game_state(mistakes, secret_word, guessed_letters):
    """Zeigt den aktuellen Zustand des Spiels an (Schneemann + Wort)."""
    # Schneemann anzeigen (entsprechend der Fehleranzahl)
    print(STAGES[mistakes])

    # Anzeige-Version des geheimen Wortes bauen
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("Word:", display_word)
    print("\n")


def play_game():
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0
    max_mistakes = len(STAGES) - 1  # letzte Stufe = komplett geschmolzen

    print("Welcome to Snowman Meltdown!")
    print("Try to save the snowman by guessing the word!")

    # Spielschleife
    while True:
        # aktuellen Zustand anzeigen
        display_game_state(mistakes, secret_word, guessed_letters)

        # Sieg-Bedingung: alle Buchstaben wurden erraten
        if all(letter in guessed_letters for letter in secret_word):
            print("🎉 You saved the snowman! The word was:", secret_word)
            break

        # Niederlage-Bedingung: Fehlerlimit erreicht
        if mistakes >= max_mistakes:
            print("💧 Oh no, the snowman melted completely!")
            print("The word was:", secret_word)
            break

        # Benutzereingabe
        guess = input("Guess a letter: ").lower().strip()

        # Eingabe validieren
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter (a-z).")
            continue

        # Schon geraten?
        if guess in guessed_letters:
            print("You already guessed that letter. Try another one.")
            continue

        # Richtiger oder falscher Buchstabe?
        if guess in secret_word:
            print("✅ Correct guess!")
            guessed_letters.append(guess)
        else:
            print("❌ Wrong guess!")
            mistakes += 1


if __name__ == "__main__":
    play_game()