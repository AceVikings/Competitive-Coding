# https://leetcode.com/problems/power-of-three/

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0 :
            return False
        if 3**29%n == 0:
            return True
        return False