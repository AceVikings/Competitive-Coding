# https://leetcode.com/problems/number-of-1-bits/

class Solution:
    def hammingWeight(self, n: int) -> int:
        j = 0
        while n != 0:
            n = n & n - 1
            j += 1

        return j