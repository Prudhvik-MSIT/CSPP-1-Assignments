'''Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob'
occurs in s. For example, if s = 'azcbobobegghakl', then your
program should print

Number of times bob occurs is: 2'''

def main():
    s = raw_input()
    # print(s)
    # the input string is in s
    # remove pass and start your code here
    count = 0
    for i in range(len(s)-3):
        if s[i:i+3] == "bob":
            count += 1
    print(count)

if __name__== "__main__":
    main()
