class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        seen = set()
        output = []
        for num in nums:
            if num in seen:
                output.append(num)
            else:
                seen.add(num)
        return output
