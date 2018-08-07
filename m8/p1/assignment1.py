'''
Author: Prudhvik Chirunomula
Date: 07-08-2018
'''
# Exercise: Assignment-1
# Write a Python function, factorial_val(n), that takes in one number and returns the factorial of given number.

# This function takes in one number and returns one number.


def factorial_val(n_val):
    '''
    n is positive Integer

    returns: a positive integer, the factorial of n.
    '''
    # Your code here
    if n_val == 0:
        return 1
    return n_val * factorial_val(n_val-1)
    


def main():
    '''main function'''
    a = input()
    print(factorial_val(int(a)))

if __name__== "__main__":
    main()
