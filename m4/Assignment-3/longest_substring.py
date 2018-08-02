'''
Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which the letters
occur in alphabetical order.

For example, if s = 'azcbobobegghakl', then your program should print

Longest substring in alphabetical order is: beggh

In the case of ties, print the first substring.
For example, if s = 'abcbcd', then your program should print

Longest substring in alphabetical order is: abc

Note: This problem may be challenging. We encourage you to work smart.
If you've spent more than a few hours on this problem, we suggest that
you move on to a different part of the course.

If you have time, come back to this problem after you've had a break and
cleared your head.
'''

def main():
    """
    main function
    """
    str_input = input()
    # the input string is in s
    # remove pass and start your code here
    seq_count = 0

    max_seq_count = 0
    max_seq_ends = 0

    for i in range(len(str_input)-1):
        # print(str_input[i],str_input[i+1])
        if ord(str_input[i]) <= ord(str_input[i+1]):
            seq_count += 1
            # print(seq_count,i)
        else:
            seq_count = 0
        if seq_count > max_seq_count:
            max_seq_count = seq_count
            max_seq_ends = i+1
    # print(max_seq_ends-max_seq_count+1,max_seq_ends)
    print(str_input[max_seq_ends-max_seq_count:max_seq_ends+1])

if __name__ == "__main__":
    main()
