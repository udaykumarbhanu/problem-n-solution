""" 844. Backspace String Compare
Given two strings S and T, return if they are equal when both are typed into empty text 
editors. # means a backspace character.

https://leetcode.com/contest/weekly-contest-87/problems/backspace-string-compare/
"""
class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        def build(word):
            ans = list()
            for c in word:
                if c != '#':
                    ans.append(c)
                else:
                    ans.pop()
            
            return "".join(ans)
        
        return build(S) == build(T)

print Solution().backspaceCompare("ab#c", "ad#c")
