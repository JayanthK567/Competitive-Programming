class Solution:
    def maximizeExpressionOfThree(self, nums: List[int]) -> int:
        largest = max(nums)
        smallest = min(nums)
        nums.remove(largest)
        second = max(nums)
        return largest+second-smallest