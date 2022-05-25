#!/usr/bin/python3
def uppercase(str):
	for letter in str:
		letter = ord(letter)
		if 97 <= letter <= 122:
			letter -= 32
		print("{:c}".format(letter), end="")
	print("")