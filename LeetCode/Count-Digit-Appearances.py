class Solution:
    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:
        seen = 0
        for num in nums:
            seen += str(num).count(str(digit))
        return seen