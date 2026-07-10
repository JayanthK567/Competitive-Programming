class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        output = []
        for i in range(0,n):
            output.append(nums[i])
            output.append(nums[i+n])
        return output