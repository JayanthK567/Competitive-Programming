class Solution:
    def largestOddNumber(self, num: str) -> str:
        right = len(num)-1
        odd = "13579"
        while right >= 0:
            if num[right] not in odd:
                right -= 1
            else:
                return num[0:right+1]
        return ""
