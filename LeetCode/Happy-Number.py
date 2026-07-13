class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n not in seen and n!=1:
            seen.add(n)
            current = 0
            for ch in str(n):
                current += int(ch)**2
            n = current

        return n == 1
