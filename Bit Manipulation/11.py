# https://leetcode.com/problems/subsets-ii
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        A = [bin(i)[2:].zfill(len(nums)) for i in range(2 ** len(nums))]
        B = []
        nums.sort()
        for i in A:
            for j in range(len(i)):
                temp = [int(nums[j] * int(i[j])) for j in range(len(i)) if (int(i[j]) != 0)]
                if temp not in B:
                    B.append(temp)
        return B
