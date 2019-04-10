'''Given two strings s and t , write a function to determine if t is an anagram
of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.
'''
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if not s and not t:
            return True
        elif not s or not t:
            return False
        else:
            d = dict()
            for char in s:
                d[char] = d.get(char, 0) + 1

            for char in t:
                d[char] = d.get(char, 0) - 1

            if any(d.values()):
                return False
            else:
                return True
            

if __name__ == '__main__':
    s = "anagram"
    t = "nagaram"

    # Expected result: True
    print Solution().isAnagram(s, t)
