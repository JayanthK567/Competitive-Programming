class Solution:
    def minMoves(self, nums: List[int]) -> int:
        largest = max(nums)
        score = 0
        for num in nums:
            score += largest - num
        return score