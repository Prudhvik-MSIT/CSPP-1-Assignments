# Assignment-3
'''
At this point, we have written code to generate a random hand and display
that hand to the user. We can also ask the user for a word (Python's
input) and score the word (using your getWordScore). However, at this
point we have not written any code to verify that a word given by a
player obeys the rules of the game. A valid word is in the word list;
and it is composed entirely of letters from the current hand. Implement
the is_valid_word function.

Testing: Make sure the test_is_valid_word tests pass. In addition, you will
want to test your implementation by calling it multiple times on the same
hand - what should the correct behavior be? Additionally, the empty string ('') is not a valid word - if you code this function correctly, you shouldn't need an additional check for this condition.

Fill in the code for is_valid_word in ps4a.py and be sure you've passed the
appropriate tests in test_ps4a.py before pasting your function definition
here.
'''

def is_valid_word(word_input, hand_dict, words_list):
    """
    Returns True if word_input is in the words_list and is entirely
    composed of letters in the hand_dict. Otherwise, returns False.

    Does not mutate hand_dict or words_list.
   
    word_input: string
    hand_dict: dictionary (string -> int)
    words_list: list of lowercase strings
    """
    # TO DO ... <-- Remove this comment when you code this function
    char_count = 0
    word_present_flag = 0
    for each_word in words_list:
        if each_word == word_input:
            word_present_flag == 1
    if not word_present_flag:
        return False
    for each_char in word_input:
        if each_char in hand_dict:
            hand_dict[each_char] -= 1
            if hand_dict[each_char] < 0:
                return False
        else:
            return False
    return True


def main():
    '''main function'''
    word = input()
    no_of_words = int(input())
    hand_dict = {}
    for _ in range(no_of_words):
        data = input()
        data = data.split()
        hand_dict[data[0]] = int(data[1])
    words_list = input().split()
    print(is_valid_word(word,hand_dict,words_list))
        


if __name__== "__main__":
    main()