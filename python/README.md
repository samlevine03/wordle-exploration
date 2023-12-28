# Wordle in Python

## Overview

Python is probably my best language, so I wanted to have a really clean implementation of the game. Admittedly, I have everything running in the `main` function. The implementation is simple and concise, eliminating the need for separate helper functions while maintaining readability and efficiency.

## Python Implementation Notes

- **Dynamic File Paths:** The script dynamically constructs paths to `words.txt` and `guesses.txt` to ensure flexibility and compatibility across different environments.
- **Simplified Logic:** The latest version features streamlined logic and leverages Python's comprehensions and built-in functions for an efficient implementation.
- **Use of `__main__` Guard:** This is a common Python practice for structuring code, allowing the script to be imported as a module in other scripts without immediately running the game. While not super necessary in this case, it's a good practice to adhere to!

## Running the Python Version

1. Navigate to the `wordle-exploration/python` directory where `wordle.py` is located.
2. Run the script using Python 3:
   ```bash
   python3 wordle.py
   ```
3. The game will start in the command-line interface.