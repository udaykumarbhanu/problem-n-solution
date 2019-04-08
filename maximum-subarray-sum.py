'''Given an integer array nums, find the contiguous subarray (containing at
least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
'''
class Solution(object):
    def maxSubArray(self, nums):
        if not nums: return 0
        
        curr_sum = max_sum = nums[0]
        for num in nums[1:]:
            curr_sum = max(num, curr_sum + num)
            max_sum = max(max_sum, curr_sum)

        return max_sum

if __name__ == '__main__':
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    # Expected output: 6, [4,-1,2,1]
    print Solution().maxSubArray(nums)
