'''Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.
'''
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        group = dict()

        for word in strs:
            key = tuple(sorted(word))
            group[key] = group.get(key, []) + [word]

        return group.values()

if __name__ == '__main__':
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    # Expected Result: [["ate","eat","tea"], ["nat","tan"],["bat"]]
    print Solution().groupAnagrams(strs)
