class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        unique = set(nums)
        output = sorted(list(unique))
        if len(output) <=2:
            return output[-1]
        else: 
            return output[-3]
