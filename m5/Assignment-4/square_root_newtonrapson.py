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
    epsilon = 0.01
    # your code starts here
    nth_guess = inp_var/2
    while nth_guess <= inp_var:
        if abs(nth_guess**2 - inp_var) >= epsilon:
            nth_guess = nth_guess - (nth_guess**2 - inp_var)/(2*nth_guess)
        else:
            break

    print(nth_guess)

if __name__ == "__main__":
    main()
