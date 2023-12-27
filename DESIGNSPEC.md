# Design Specification

## Overview

This document outlines the design specifications for the Wordle-like command-line game implemented in multiple programming languages. The game will follow a consistent set of rules and feedback symbols across all implementations.

## Game Rules

1. **Objective:** The player's goal is to guess a secret word within a limited number of attempts.
2. **Word List:** The secret word is selected from a list of words contained in `words.txt`.
3. **Legal Guesses:** In addition to the words in `words.txt`, players can make guesses from an additional list of legal words found in `guesses.txt`. So guesses should be checked against the words from both files for validity. 
4. **Word Length:** Each secret word is exactly 5 letters long.
5. **Number of Guesses:** Players have 6 attempts to guess the word correctly.
6. **Guess Validation:** Only valid 5-letter words from `words.txt` and `guesses.txt` are accepted as guesses. Implementations should handle and inform invalid inputs accordingly.

## Feedback Mechanism

After each guess, the player receives feedback for each letter in the guessed word:

- `*` (Asterisk): The letter is correct and in the correct position.
- `?` (Question Mark): The letter is correct but in the wrong position.
- `.` (Period): The letter is not in the word.

## Interface

### Example Gameplay: Winning Scenario

```plaintext
Welcome to Wordle!

Enter guess 1/6:
> trace
  .*?*?

Enter guess 2/6:
> crane
  *****

Congratulations! You guessed the word!

Game Over. You won in 2 attempts!
```

#### Losing Secnario

```plaintext
Welcome to Wordle!

Enter guess 1/6:
> apple
  .....

Enter guess 2/6:
> great
  *....

Enter guess 3/6:
> clear
  ..*..

Enter guess 4/6:
> crate
  **...

Enter guess 5/6:
> charm
  **...

Enter guess 6/6:
> chase
  **...

Sorry, you didn't guess the word.
The correct word was 'crane'.

Game Over. Better luck next time!
```

#### Invalid or Repeat Guesses

```plaintext
Welcome to Wordle!

Enter guess 1/6:
> brave
  .....

Enter guess 2/6:
> brav
Invalid input: Guess must be 5 letters. Try again.

Enter guess 2/6:
> brave
Invalid input: Repeat guess. Try again.

Enter guess 2/6:
> baave
Invalid input: Not in word list. Try again.
```