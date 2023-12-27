# Design Specification

## Overview

This document outlines the design specifications for the Wordle-like command-line game implemented in multiple programming languages. The game will follow a consistent set of rules and feedback symbols across all implementations.

## Game Rules

1. **Objective:** The player's goal is to guess a secret word within a limited number of attempts.
2. **Word Length:** Each secret word is exactly 5 letters long.
3. **Number of Guesses:** Players have 6 attempts to guess the word correctly.
4. **Guess Validation:** Only valid 5-letter words are accepted as guesses. Implementations should handle and inform invalid inputs accordingly.

## Feedback Mechanism

After each guess, the player receives feedback for each letter in the guessed word:

- `*` (Asterisk): The letter is correct and in the correct position.
- `?` (Question Mark): The letter is correct but in the wrong position.
- `.` (Period): The letter is not in the word

## Interface

### Example Gameplay

#### Winning Scenario

```plaintext
Welcome to Wordle!

Enter your guess:
> trace
Feedback: .*?*?

Enter your guess:
> crane
Feedback: *****

Congratulations! You guessed the word!

Game Over. You won in 2 attempts!
```

#### Losing Secnario

```plaintext
Welcome to Wordle!

Enter your guess:
> apple
Feedback: .....

Enter your guess:
> great
Feedback: *....

Enter your guess:
> clear
Feedback: ..*..

Enter your guess:
> crate
Feedback: **...

Enter your guess:
> charm
Feedback: **...

Enter your guess:
> chase
Feedback: **...

Sorry, you didn't guess the word.
The correct word was 'crane'.

Game Over. Better luck next time!
```

#### Invalid or Repeat Guesses

```plaintext
Welcome to Wordle!

Enter your guess:
> brave
Feedback: .....

Enter your guess:
> brav
Invalid input: Guess must be 5 letters. Try again.

Enter your guess:
> brave
Invalid input: Repeat guess. Try a different word.
```