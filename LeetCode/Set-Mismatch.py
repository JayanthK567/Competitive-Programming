class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        seen = set()
        output = []
        for num in nums:
            if num in seen:
                output.append(num)
            seen.add(num)
        for i in range(1,len(nums)+1):
            if i not in seen:
                output.append(i)
        return output