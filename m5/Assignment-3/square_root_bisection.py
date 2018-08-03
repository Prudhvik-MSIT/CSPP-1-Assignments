# Write a python program to find the square root of the given number
# using approximation method

# testcase 1
# input: 25
# output: 4.999999999999998

# testcase 2
# input: 49
# output: 6.999999999999991

EPSILON = 0.01
INPUT_VAR = int(input())
# your code starts here

LO_GUESS = 0
HI_GUESS = INPUT_VAR

GUESS = (LO_GUESS+HI_GUESS)/2

while abs(GUESS**2 - INPUT_VAR) >= EPSILON:
	if GUESS**2 < INPUT_VAR:
		LO_GUESS = GUESS
	else:
		HI_GUESS = GUESS
	GUESS = (LO_GUESS + HI_GUESS)/2

print(GUESS)