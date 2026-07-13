class Solution:
    def checkDivisibility(self, n: int) -> bool:
        total = 0
        product = 1
        initial = n
        while n > 0:
            current = n%10
            total += current
            product *= current
            n //= 10
        if (total+product) == 0:
            return False
        return initial%(total+product) == 0