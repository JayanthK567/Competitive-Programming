class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        output = [-1,-1]
        left = 0
        right = len(nums)-1
        i = 0
        while i<len(nums):
            if nums[left] == target:
                output[0] = left
            else: 
                left += 1

            if nums[right] == target:
                output[1] = right
            else:
                right -= 1
            i += 1
        return output