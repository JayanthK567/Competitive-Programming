class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        clean = set(nums)
        output = []
        for i in range(len(nums)):
            if i+1 not in clean:
                output.append(i+1)
        return output