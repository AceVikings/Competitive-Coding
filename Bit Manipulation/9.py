# https://leetcode.com/problems/counting-bits/

class Solution:
    def countBits(self, n: int) -> List[int]:
        A = [bin(i).count('1') for i in range(n+1)]
        return A