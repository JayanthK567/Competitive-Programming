class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        score = 0
        if word not in sequence:
            return score
        else:
            for k in range(1,len(sequence)+1):
                if word*k in sequence:
                    score += 1
        return score