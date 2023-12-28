# Wordle in Python

## Overview

I learned some basic Ruby (more specifically Rails) very recently, and found the learning curve quite friendly since the language is a lot like Python. 

## Ruby Implementation Notes

- **Dynamic File Paths:** The Ruby script uses the `Pathname` library to construct paths to `words.txt` and `guesses.txt`, ensuring compatibility across different environments and enhancing code readability. 
- **Simplified Logic:** Leveraging Ruby's expressive syntax, the feedback generation logic in the `score` method is both concise and efficient. The use of `each_char` and `zip` elegantly handles the comparison of characters in the secret word and the guess. It's almost a "functional" approach. 
- **Ruby's Set for Guess Tracking:** The use of Ruby's `Set` class for storing guesses efficiently handles repeat guess validation.

## Running the Ruby Version

1. Navigate to the `wordle-exploration/ruby` directory where `wordle.rb` is located.
2. Run the script using Ruby:
   ```bash
   ruby wordle.rb
   ```
3. The game will start in the command-line interface.