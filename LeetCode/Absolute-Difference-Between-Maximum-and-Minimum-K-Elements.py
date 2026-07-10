class Solution:
    def absDifference(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        return abs(sum(nums[:k]) - sum(nums[len(nums)-k:]))