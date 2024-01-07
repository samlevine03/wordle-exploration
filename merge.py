# https://gist.github.com/nshafer/8e12aa557cc91c6b16a6057e83e4741e
# I missed some words. To add new words to wordlist.txt, put them in new.txt in alphabetical order, then run this script.

def merge_and_sort_files(file1, file2, output_file):
    # Read words from first file
    with open(file1, 'r') as f:
        words1 = f.read().splitlines()

    # Read words from second file
    with open(file2, 'r') as f:
        words2 = f.read().splitlines()

    # Combine and sort the lists
    combined_words = sorted(set(words1 + words2))

    # Write the sorted words back to the output file
    with open(output_file, 'w') as f:
        for word in combined_words:
            f.write(word + '\n')

# Example usage
merge_and_sort_files('wordlist.txt', 'new.txt', 'wordlist.txt')  # This will update 'wordlist.txt' with the sorted list