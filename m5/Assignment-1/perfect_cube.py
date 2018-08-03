"""
# Write a python program to find if the given number is a perfect cube or not
# using guess and check algorithm

# testcase 1
# Input: 24389
# Output: 24389 is a perfect cube

# testcase 2
# Input: 21950
# Output: 21950 is not a perfect cube
"""
def main():
    """
    # input is captured in s
    """
    input_var = int(input())
    # watch out for the data type of value stored in s
    # your code starts here
    guess_val = 0

    while guess_val**3 < input_var:
        guess_val += 1

    if guess_val**3 == input_var:
        print(str(input_var)+" is a perfect cube")
    else:
        print(str(input_var)+" is not a perfect cube")

if __name__ == "__main__":
    main()
