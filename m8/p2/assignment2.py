'''
Author: Prudhvik Chirunomula
Date: 07-08-2018
'''
# Exercise: Assignment-2
# Write a Python function, sum_of_digits, that takes in one number
# and returns the sum of digits of given number.

# This function takes in one number and returns one number.

def sum_of_digits(n_val):
    '''
    n is positive Integer

    returns: a positive integer, the sum of digits of n.
    '''
    # Your code here
    if n_val == 0:
        return 0
    return n_val%10 + sum_of_digits(n_val//10)

def main():
    '''main function'''
    a_val = input()
    print(sum_of_digits(int(a_val)))

if __name__ == "__main__":
    main()
