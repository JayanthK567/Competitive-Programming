class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        small = 99999
        large = -99999
        output = []
        if len(nums)==0:
            return output
        for num in set(nums):
            small = min(small,num)
            large = max(large,num)
        for i in range(small,large+1):
            if i not in nums:
                output.append(i)
        return output