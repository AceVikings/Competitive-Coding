# https://leetcode.com/problems/missing-number/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        temp = 0
        for i in range(len(nums) + 1):
            temp ^= i
        for j in nums:
            temp ^= j

        return temp
