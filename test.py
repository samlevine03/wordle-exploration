import argparse
import subprocess

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

def run_game_with_args(executable, args, cwd):
    command = executable + args
    process = subprocess.Popen(
        command,
        stdout=subprocess.PIPE,
        text=True,
        cwd=cwd
    )

    output, _ = process.communicate()
    return output

def test_wordle_info(language):
    game_path = LANGUAGE_PATHS[language]
    cwd = LANGUAGE_CWD[language]
    info_arg = ['--info']
    output = run_game_with_args(game_path, info_arg, cwd)

    # Validate output for --info
    assert '2309' in output
    assert '12947' in output

def test_wordle_with_secret(language, secret, guesses, expected_feedback):
    if language not in LANGUAGE_PATHS:
        raise ValueError(f"Unsupported language: {language}")

    game_path = LANGUAGE_PATHS[language]
    cwd = LANGUAGE_CWD[language]
    secret_arg = ['-s', secret]
    command = game_path + secret_arg
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
        assert '> ' in f

def test_wordle_with_invalid_guesses(language, secret, guesses):
    if language not in LANGUAGE_PATHS:
        raise ValueError(f"Unsupported language: {language}")

    game_path = LANGUAGE_PATHS[language]
    cwd = LANGUAGE_CWD[language]
    secret_arg = ['-s', secret]
    command = game_path + secret_arg
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


def main():
    parser = argparse.ArgumentParser(description="Test the Wordle game.")
    parser.add_argument('language', type=str, help="Language of the Wordle game to test (e.g., 'python', 'ruby')")
    args = parser.parse_args()

    # Test game information output
    test_wordle_info(args.language)

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

if __name__ == '__main__':
    main()
