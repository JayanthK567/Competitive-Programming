class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        i = 1
        while i<999:
            if i*k not in nums:
                return i*k
                break
            i += 1
        return -1