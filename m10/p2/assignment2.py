'''
Exercise : Assignment-2
implement the function hangman, which takes one parameter - the secret_word
the user is to guess. This starts up an interactive game of Hangman between
the user and the computer. Be sure you take advantage of the three helper functions,
isWordGuessed, getGuessedWord, and getAvailableLetters,
that you've defined in the previous part.
'''

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # in_file: file
    in_file = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = in_file.readline()
    # word_list: list of strings
    word_list = line.split()
    print("  ", len(word_list), "words loaded.")
    return word_list

def chooseord(words_list):
    """
    words_list (list): list of words (strings)

    Returns a word from words_list at random
    """
    return random.choice(words_list)

# end of helper code
# -----------------------------------

# Load the list of words into the variable LIST_OF_WORDS
# so that it can be accessed from anywhere in the program
LIST_OF_WORDS = load_words()

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    guessed_word = "_"*len(secret_word)
    success_flag = 0
    for guesses_left in range(len(secret_word)+3, 0, -1):
        if guessed_word == secret_word:
            success_flag = 1
            break
        print("Guessed word so far: "+str(guessed_word))#,secret_word)
        guess = input("You have "+str(guesses_left)+" guesses left\nEnter your guess: ")
        for iter_no, iter_char in enumerate(secret_word):
            if guess == iter_char:
                guessed_word = guessed_word[:iter_no]+guess+guessed_word[iter_no+1:]
    if success_flag:
        print("Congratulations!!")
    else:
        print("Oops!! the correct word is: "+secret_word)


def main():
    '''
    Main function for the given program

    When you've completed your hangman function, uncomment these two lines
    and run this file to test! (hint: you might want to pick your own
    secret_word while you're testing)
    '''
    secret_word = chooseord(LIST_OF_WORDS).lower()
    hangman(secret_word)


if __name__ == "__main__":
    main()
