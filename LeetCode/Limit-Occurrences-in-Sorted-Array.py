class Solution:
    def limitOccurrences(self, nums: list[int], k: int) -> list[int]:
        for num in nums:
            while nums.count(num) > k:
                nums.remove(num)
        return nums