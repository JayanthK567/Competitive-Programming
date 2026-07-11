class Solution:
    def maxKDistinct(self, nums: List[int], k: int) -> List[int]:
        nums = sorted(set(nums))
        if k >= len(nums):
            return nums[::-1]
        else:
            return nums[len(nums):len(nums)-k-1:-1]
