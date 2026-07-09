class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:
        for num in nums:
            if nums.count(num) < 2 and num%2 == 0:
                return num
        return -1