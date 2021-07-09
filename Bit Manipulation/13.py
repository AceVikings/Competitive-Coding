# https://leetcode.com/problems/repeated-dna-sequences
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        Dict = {}
        A = []
        for i in range(len(s)-9):
            temp = s[i:i+10] 
            if temp in Dict and temp not in A:
                A.append(temp)
            else:
                Dict[temp] = 1
        return A