class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        output = []
        for num in nums:
            if num%2 == 0:
                output.append(num)
        for num in nums:
            if num%2 != 0:
                output.append(num)
        return output