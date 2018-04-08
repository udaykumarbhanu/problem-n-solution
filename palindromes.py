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


def palindrome_three(s):
	"""
	:type s: string
	:rtype: boolean
	"""
	if s:
		start_index = 0
		end_index = len(s) - 1

		while start_index < end_index:
			if s[start_index] != s[end_index]:

				return False
			else:
				start_index += 1
				end_index -= 1

		return True

	else: 
		# None(null) is not palindrome.
		
		return False


if __name__ == "__main__":
	s1="aba"
	print palindrome_one(s1)
	
	s2="donna"
	print palindrome_two(s2)

	s3="uday"
	print palindrome_three(s3)
