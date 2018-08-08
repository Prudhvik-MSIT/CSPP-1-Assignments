"""Given a  number int_input, find the product of all the digits"""
def main():
    '''
    Read any number from the input, store it in variable int_input.
    '''
    n_inp = int(input())
    res_out = 1
    neg_flag = 1
    if n_inp < 0:
        neg_flag = -1
        n_inp *= neg_flag
    if n_inp == 0:
        print(0)
    else:
        while n_inp > 0:
            res_out *= n_inp%10
            n_inp //= 10
        print(res_out*neg_flag)

if __name__ == "__main__":
    main()