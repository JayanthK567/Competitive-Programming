class Solution:
    def validDigit(self, n: int, x: int) -> bool:
        output = False
        while n > 0:
            if x == n%10:
                output = True
                if n < 10:
                    output = False
            n = n//10
        return output