# https://leetcode.com/problems/power-of-four
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        if (not (n & (n - 1))):
            temp = 0
            while (n > 1):
                n >>= 1
                temp += 1
            if temp % 2 == 0:
                return True
            return False

        return False