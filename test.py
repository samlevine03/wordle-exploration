import argparse
import subprocess
import shutil
import os

LANGUAGE_PATHS = {
    'python': ['python3', 'wordle.py'],
    'ruby': ['ruby', 'wordle.rb'],
    # Add other languages and their paths here
}
LANGUAGE_CWD = {
    'python': 'python/',
    'ruby': 'ruby/',
    # Add other languages and their cwd here
}

def modify_words_file(temp_word, words_path, backup_words_path):
    # Backup the original words.txt
    shutil.copyfile(words_path, backup_words_path)

    # Write the temporary word to words.txt
    with open(words_path, 'w') as file:
        file.write(temp_word + '\n')

def modify_guesses_file(temp_guesses, guesses_path, backup_guesses_path):
    # Backup the original guesses.txt
    shutil.copyfile(guesses_path, backup_guesses_path)

    # Write the temporary guesses to guesses.txt (guesses is a list of words)
    with open(guesses_path, 'w') as file:
        for guess in temp_guesses:
            file.write(guess + '\n')
    
def restore_file(file_path, backup_path):
    # Restore the original words.txt
    shutil.move(backup_path, file_path)

def test_wordle_with_secret(language, secret, guesses, expected_feedback):
    if language not in LANGUAGE_PATHS:
        raise ValueError(f"Unsupported language: {language}")

    game_path = LANGUAGE_PATHS[language]
    cwd = LANGUAGE_CWD[language]
    words_path = 'words.txt'
    backup_path = words_path + '.bak'
    guesses_path = 'guesses.txt'
    backup_guesses_path = guesses_path + '.bak'

    try:
        modify_words_file(secret, words_path, backup_path)
        modify_guesses_file(guesses, guesses_path, backup_guesses_path)

        command = game_path
        process = subprocess.Popen(
            command,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            text=True,
            cwd=cwd
        )

        output, _ = process.communicate('\n'.join(guesses))

        for i in range(1, len(guesses) + 1):
            assert f"{i}/6" in output

        output = output.split('\n')
        
        assert "Welcome to Wordle!" in output[0]
        feedback = [output[i] for i in range(len(output)) if i != 0 and i % 2 == 0]
        for f, ef in zip(feedback, expected_feedback):
            assert ef in f

    finally:
        restore_file(words_path, backup_path)
        restore_file(guesses_path, backup_guesses_path)

def test_wordle_with_invalid_guesses(language, secret, guesses):
    if language not in LANGUAGE_PATHS:
        raise ValueError(f"Unsupported language: {language}")

    game_path = LANGUAGE_PATHS[language]
    cwd = LANGUAGE_CWD[language]
    words_path = 'words.txt'
    backup_path = words_path + '.bak'
    guesses_path = 'guesses.txt'
    backup_guesses_path = guesses_path + '.bak'

    try:
        modify_words_file(secret, words_path, backup_path)
        modify_guesses_file(["stare"], guesses_path, backup_guesses_path)

        command = game_path
        process = subprocess.Popen(
            command,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            text=True,
            cwd=cwd
        )

        output, _ = process.communicate('\n'.join(guesses))

        assert '1/6' in output
        assert '2/6' in output
        assert '3/6' not in output
        assert '4/6' not in output
        assert '5/6' not in output
        assert '6/6' not in output

        output = output.split('\n')
        feedback = [output[i] for i in range(len(output)) if i != 0 and i % 2 == 0]

        assert "5 letters" in feedback[0]
        assert "word list" in feedback[1]
        assert "Repeat" in feedback[3]

    finally:
        restore_file(words_path, backup_path)
        restore_file(guesses_path, backup_guesses_path)


def main():
    parser = argparse.ArgumentParser(description="Test the Wordle game.")
    parser.add_argument('language', type=str, help="Language of the Wordle game to test (e.g., 'python', 'ruby')")
    args = parser.parse_args()

    # Test gameplay with specific secret word
    secret = 'stare'
    guesses = ['trace', 'slate', 'stare']
    expected_feedback = ['??*.*', '*.*?*', '*****']
    test_wordle_with_secret(args.language, secret, guesses, expected_feedback)

    secret = 'climb'
    guesses = ['stare', 'shape', 'block', 'cling', 'forty', 'climb']
    expected_feedback = ['.....', '.....', '?*.?.', '***..', '.....', '*****']
    test_wordle_with_secret(args.language, secret, guesses, expected_feedback)

    secret = 'finch'
    guesses = ['conch', 'finch']
    expected_feedback = ['..***', '*****']
    test_wordle_with_secret(args.language, secret, guesses, expected_feedback)

    secret = 'guess'
    guesses = ['bleed', 'guess']
    expected_feedback = ['..*..', '*****']
    test_wordle_with_secret(args.language, secret, guesses, expected_feedback)

    secret = 'queue'
    guesses = ['bleed', 'queue']
    expected_feedback = ['..*?.', '*****']
    test_wordle_with_secret(args.language, secret, guesses, expected_feedback)

    secret = 'bleed'
    guesses = ['geese', 'bleed']
    expected_feedback = ['.?*..', '*****']
    test_wordle_with_secret(args.language, secret, guesses, expected_feedback)

    secret = 'brave'
    guesses = ['barv', 'bbbbb', 'stare', 'stare', 'brave']
    test_wordle_with_invalid_guesses(args.language, secret, guesses)

    print("All tests passed successfully.")

if __name__ == '__main__':
    main()
