class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        A = [bin(i)[2:].zfill(len(nums)) for i in range(2 ** len(nums))]
        B = []
        chars = [str(i) for i in nums]
        for i in A:
            B.append([int(chars[j] * int(i[j])) for j in range(len(i)) if int(i[j]) != 0])

        return B
