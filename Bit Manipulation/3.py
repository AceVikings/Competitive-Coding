# https://leetcode.com/problems/reverse-bits/
class Solution:
    def reverseBits(self, n: int) -> int:
        num = bin(n)
        reverse = num[-1:1:-1]
        reverse = reverse + (32-len(reverse))*'0'
        return (int(reverse,2))