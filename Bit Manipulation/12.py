# https://leetcode.com/problems/gray-code/
class Solution:
    def grayCode(self, n: int) -> List[int]:
        A = [i^(i>>1) for i in range(0,2**(n))]
        return A