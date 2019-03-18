''' Start from integer 1, remove any integer that contains 9 such as 9,
19, 29...

So now, you will have a new integer sequence: 1, 2, 3, 4, 5, 6, 7, 8, 10, 11, ...

Given a positive integer n, you need to return the n-th integer after removing. Note that 1 will be the first integer.

Example 1:
Input: 9
Output: 10
'''
class Solution(object):
    def newInteger(self, n):
        if n<9:
            return n

        result = ''
        while n>0:
            result = str(n%9) + result
            n /= 9

        return int(result)

if __name__ == '__main__':
    n = 19
    print Solution().newInteger(n)
