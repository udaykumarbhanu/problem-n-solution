#Problem URL: https://www.geeksforgeeks.org/check-whether-two-strings-are-anagram-of-each-other/

# Problem: Check whether two strings are anagram of each other.

def areAnagram(first_str, second_str):
	if len(first_str) != len(second_str):
		return False

	# sort both the string, first convert them to list and then apply sort and compare.
	first_str = list(first_str)
	second_str = list(second_str)

	first_str.sort()
	second_str.sort()

	# print first_str, second_str

	if first_str == second_str:
		return True
	else: 
		return False

if __name__ == "__main__":
	print areAnagram("act", "cat")