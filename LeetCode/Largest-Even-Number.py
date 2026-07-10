class Solution:
    def largestEven(self, s: str) -> str:
        if s == '':
            return ''
        else:
            right = len(s)-1
            while s[right] != '2' and right>=0:
                right -= 1
            return s[:right+1]