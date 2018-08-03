"""
#Assume s is a string of lower case characters.

#Write a program that counts up the number of vowels contained in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if s = 'azcbobobegghakl', your program should print:

#Number of vowels: 5
"""
def main():
	"""
	#your code here
	"""
	number_of_test_cases = int(input())
	for _ in range(number_of_test_cases):
		inp_str = input()
		count_vow = 0
		for i in inp_str:
			if i in "aeiou":
				count_vow += 1
		print(count_vow)

if __name__== "__main__":
	main()