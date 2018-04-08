def reverse_one(s):
	reversed = ""

	for char in s:
		reversed = char + reversed

	return reversed


def reverse_two(s):
	s_arr = list(s)
	s_arr.reverse()

	return "".join(s_arr)
	

def reverse_three(s):

	return s[::-1]

if __name__ == "__main__":
	s = "uday"
	print reverse_one(s)
	print reverse_two(s)
	print reverse_three(s)

