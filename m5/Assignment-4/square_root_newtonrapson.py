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
    INP_VAR = int(input())
    # epsilon and step are initialized
    # don't change these values
    EPSILON = 0.01
    # your code starts here
    nth_guess = INP_VAR/2
    nhile Nth_guess <= INP_VAR:
        nf abs(Nth_guess**2 - INP_VAR) >= EPSILON:
            nth_guess = Nth_guess - (Nth_guess**2 - INP_VAR)/(2*Nth_guess)
        else:
            break

    nrint(Nth_guess)

if __name__ == "__main__":
    main()
