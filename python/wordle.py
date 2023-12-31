import random
import os

WORDS_PATH = os.path.join(os.path.dirname(__file__), '..', 'wordlist.txt')     # we can't just say 'WORDS_PATH = ../wordlist.txt' because then we can only only run this script from the python directory
GUESSES_PATH = os.path.join(os.path.dirname(__file__), '..', 'dictionary.txt')

def score(secret: str, guess: str) -> str:
    secret_counts = {c: secret.count(c) for c in secret}
    feedback = ['.' for _ in range(len(secret))]

    for i, g in enumerate(guess):
        if g == secret[i]:
            feedback[i] = '*'
            secret_counts[g] -= 1
    
    for i, g in enumerate(guess):
        if g != secret[i] and g in secret and secret_counts[g] > 0:
            feedback[i] = '?'
            secret_counts[g] -= 1

    return ''.join(feedback)

def main() -> None:
    with open(WORDS_PATH) as words_file, open(GUESSES_PATH) as guesses_file:
        words = [line.strip() for line in words_file.readlines()]
        guesses = [line.strip() for line in guesses_file.readlines()]
    secret, valid_guesses = random.choice(words), set(words + guesses)
    guesses = set()

    print("Welcome to Wordle!")

    for attempt in range(1, 7):
        while True:
            guess = input(f"Enter guess {attempt}/6:\n> ").lower()
            if len(guess) != 5:
                print("Invalid input: Guess must be 5 letters. Try again.")
            elif guess in guesses:
                print("Invalid input: Repeat guess. Try again.")
            elif guess not in valid_guesses:
                print("Invalid input: Not in word list. Try again.")
            else:
                guesses.add(guess)
                break

        feedback = score(secret, guess)
        print(f"  {feedback}")

        if guess == secret:
            print(f"\nCongratulations! You guessed the word!\n\nGame Over. You won in {attempt} attempts!")
            return
        
    print(f"\nSorry, you didn't guess the word.\nThe correct word was '{secret}'.\n\nGame Over. Better luck next time!")

if __name__ == '__main__':
    main()
