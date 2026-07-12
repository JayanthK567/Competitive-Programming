class Solution:
    def minimumCost(self, nums: list[int], k: int) -> int:
        nums.sort()
        score1 = k
        cost = 0
        n = 0
        for i in range(len(nums)):
            if nums[i] > score1:
                gap = (nums[i] - score1 + k -1)//k
                n += gap
                score1 += k * gap
            if nums[i] <= score1: # comparing score1 to value of num
                score1 -= nums[i] #recuding score1 if k available
        cost = (n*(n+1))//2
        return cost % ((10**9) +7)