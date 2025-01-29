import random

def choose_word():
    """Selects a random word from a predefined list."""
    word_list = ["python", "hangman", "programming", "developer", "challenge", "function"]
    return random.choice(word_list).lower()

def display_word(word, guessed_letters):
    """Displays the word with guessed letters revealed."""
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])

def hangman():
    """Main function to run the Hangman game."""
    print("Welcome to Hangman!")
    word = choose_word()
    guessed_letters = set()
    attempts_remaining = 6

    while attempts_remaining > 0:
        print("\n" + display_word(word, guessed_letters))
        print(f"Attempts remaining: {attempts_remaining}")
        print(f"Guessed letters: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}")

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print(f"Good job! '{guess}' is in the word.")
        else:
            print(f"Sorry, '{guess}' is not in the word.")
            attempts_remaining -= 1

        if all(letter in guessed_letters for letter in word):
            print("\nCongratulations! You guessed the word:", word)
            break
    else:
        print("\nGame over! The word was:", word)

if __name__ == "__main__":
    hangman()
