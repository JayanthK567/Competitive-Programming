class Solution:
    def checkGoodInteger(self, n: int) -> bool:
        digitsum = 0
        squaresum = 0
        while n > 0:
            digitsum += n%10
            squaresum += (n%10)**2
            n = n//10
        return squaresum - digitsum >= 50