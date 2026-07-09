class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        rev = 0
        sec = x
        while sec>0:
            rev = (rev*10)+(sec%10)
            sec = sec//10
        return rev == x
