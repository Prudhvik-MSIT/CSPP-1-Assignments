'''
Replace all the special characters(!, @, #, $, %, ^, &, *) in a given string with a space.
example : ab!@#cd is the input, the output is ab   cd
Output has three spaces, which are to be replaced with these special characters
'''
def main():
    '''
    Read string from the input, store it in variable str_input.
    '''
    STR_INPUT = input()
    S_OUT = ""
    for char in STR_INPUT:
        if char == '!' or char == '@' or char == '#' or char == '$' or char == '%' or char == '^' or char == '&' or char == '*':
            S_OUT = S_OUT + " "
        else:
            S_OUT = S_OUT + char
    print(S_OUT)
if __name__ == "__main__":
    main()