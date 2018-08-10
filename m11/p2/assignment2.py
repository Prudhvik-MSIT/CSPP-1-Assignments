'''
Exercise: Assignment-2
Implement the update_hand function. Make sure this function has no side
effects: i.e., it must not mutate the hand_dict passed in. Before pasting
your function definition here, be sure you've passed the appropriate
tests in test_ps4a.py.
'''

def update_hand(hand_dict, word_given):
    """
    Assumes that 'hand_dict' has all the letters in word_given.
    In other word_givens, this assumes that however many times
    a letter appears in 'word_given', 'hand_dict' has at least as
    many of that letter in it.

    Updates the hand_dict: uses up the letters in the given word_given
    and returns the new hand_dict, without those letters in it.

    Has no side effects: does not modify hand_dict.

    word_given: string
    hand_dict: dictionary (string -> int)
    returns: dictionary (string -> int)
    """
    # TO DO ... <-- Remove this comment when you code this function
    for each_char in word_given:
        if each_char in hand_dict:
            hand_dict[each_char] -= 1
    return hand_dict

def main():
    '''main function'''
    no_of_inputs = input()
    adict = {}
    for _ in range(int(no_of_inputs)):
        data = input()
        list_of_data = data.split()
        adict[list_of_data[0]] = int(list_of_data[1])
    data1 = input()
    print(update_hand(adict, data1))

if __name__ == "__main__":
    main()
