class Solution:
    def reverseDegree(self, s: str) -> int:
        score = 0
        for i in range(len(s)):
            value = (123 - ord(s[i]))
            score += value * (i+1)
        return score
