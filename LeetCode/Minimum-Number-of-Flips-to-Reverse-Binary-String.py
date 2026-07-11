class Solution:
    def minimumFlips(self, n: int) -> int:
        binary = format(n,'b')
        rev = binary[::-1]
        score = 0
        for i in range(len(binary)):
            if binary[i] != rev[i]:
                score += 1
        return score
