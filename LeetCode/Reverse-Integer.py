class Solution:
    def reverse(self, x: int) -> int:
        duplicate = abs(x)
        output= 0
        while duplicate > 0:
            current = duplicate % 10
            output = (output*10) + current
            duplicate //= 10
        if output> (2**31)-1 or output< (2**31)*(-1):
            return 0
        if x < 0:
            return output * -1
        else: 
            return output