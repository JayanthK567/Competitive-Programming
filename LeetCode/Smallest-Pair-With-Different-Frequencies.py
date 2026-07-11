class Solution:
    def minDistinctFreqPair(self, nums: list[int]) -> list[int]:
        if len(nums) <= 2:
            return [-1,-1]
        seen = {}
        nums = sorted(nums)
        for num in nums:
            seen[num] = seen.get(num,0)+1 #count frequency
        freq = set()
        output = []
        for key in seen:
            if seen[key] not in freq and len(output) <2:
                output.append(key)
                freq.add(seen[key])
        if len(output) < 2:
            return [-1,-1]
        else:
            return sorted(output)
