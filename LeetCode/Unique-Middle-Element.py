class Solution:
    def isMiddleElementUnique(self, nums: list[int]) -> bool:
        if len(nums) == 1:
            return True
        else:
            return nums.count(nums[len(nums)//2]) == 1