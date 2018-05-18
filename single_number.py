"""
https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/549/

Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
"""

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = nums[0]
        for i in range(1, len(nums)):
            result = result ^ nums[i]
        
        return result

print Solution().singleNumber([1,1,2])
