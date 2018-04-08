def palindrome_one(s):
	"""
	:type s: string
	:rtype: boolean
	"""
	reversed = ""
	for char in s:
		reversed = char + reversed

	return s == reversed


def palindrome_two(s):
	"""
	:type s: string
	:rtype: boolean
	"""

	return s == s[::-1]


if __name__ == "__main__":
	s1="aba"
	print palindrome_one(s1)
	
	s2="chasmish"
	print palindrome_two(s2)