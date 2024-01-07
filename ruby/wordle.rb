require 'set'
require 'pathname'

WORDS_PATH = Pathname.new(__FILE__).dirname.join('..', 'wordlist.txt').realpath.to_s
GUESSES_PATH = Pathname.new(__FILE__).dirname.join('..', 'dictionary.txt').realpath.to_s

def score(secret, guess)
  secret_counts = Hash.new(0)
  secret.each_char { |c| secret_counts[c] += 1 }

  feedback = '.....'
  
  (0...secret.length).each do |i|
    if secret[i] == guess[i]
      feedback[i] = '*'
      secret_counts[guess[i]] -= 1
    end
  end

  (0...secret.length).each do |i|
    if secret[i] != guess[i] && secret_counts[guess[i]] > 0
      feedback[i] = '?'
      secret_counts[guess[i]] -= 1
    end
  end

  feedback
end


def main
  words = File.readlines(WORDS_PATH).map(&:strip)
  guesses = File.readlines(GUESSES_PATH).map(&:strip)
  valid_guesses = Set.new(words + guesses)

  secret = words.sample
  attempts = Set.new

  puts "Welcome to Wordle!"

  6.times do |attempt|
    guess = nil
    loop do
      print "Enter guess #{attempt + 1}/6:\n> "
      guess = gets.chomp.downcase

      if guess.length != 5
        puts "Invalid input: Guess must be 5 letters. Try again."
      elsif attempts.include?(guess)
        puts "Invalid input: Repeat guess. Try again."
      elsif !valid_guesses.include?(guess)
        puts "Invalid input: Not in word list. Try again."
      else
        attempts.add(guess)
        break
      end
    end

    feedback = score(secret, guess)
    puts "  #{feedback}"

    if guess == secret
      puts "\nCongratulations! You guessed the word!\n\nGame Over. You won in #{attempt + 1} attempts!"
      return
    end
  end

  puts "\nSorry, you didn't guess the word.\nThe correct word was '#{secret}'.\n\nGame Over. Better luck next time!"
end

main if __FILE__ == $PROGRAM_NAME
