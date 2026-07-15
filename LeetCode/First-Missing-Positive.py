class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = set(nums)
        for i in range(1,max(nums)+1,1):
            if i not in nums:
                return i
        return max(1,max(nums)+1)