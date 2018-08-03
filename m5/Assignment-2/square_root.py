"""
# Write a python program to find the square root of the given number
# using approximation method

# testcase 1
# input: 25
# output: 4.999999999999998

# testcase 2
# input: 49
# output: 6.999999999999991
"""
def main():
    """
    main function
    """
    inp_var = int(input())
    # epsilon and step are initialized
    # don't change these values
    epsilon_value = 0.01
    step_inc = 0.1
    # your code starts here
    guess_val = 0
    while abs(guess_val**2 - inp_var) >= epsilon_value:
        guess_val += step_inc
    print(guess_val)

if __name__ == "__main__":
    main()
