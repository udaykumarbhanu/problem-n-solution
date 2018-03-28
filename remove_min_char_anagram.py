# Problem: https://www.geeksforgeeks.org/remove-minimum-number-characters-two-strings-become-anagram/

"""Input : str1 = "bcadeh" str2 = "hea"
Output: 3
We need to remove b, c and d from str1.
"""

def remMinCharAnagram(s1, s2):
	diff_char = list(s1)

	for char in s2:
		if char in diff_char:
			diff_char.remove(char)

	return len(diff_char)

if __name__ == "__main__":
	print remMinCharAnagram(s1="bcadeh", s2="hea")