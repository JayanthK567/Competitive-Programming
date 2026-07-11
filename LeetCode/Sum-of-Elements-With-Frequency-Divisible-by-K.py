class Solution:
    def sumDivisibleByK(self, nums: List[int], k: int) -> int:
        seen = {}
        total = 0
        for num in nums:
            seen[num] = seen.get(num,0)+1
        for num in seen:
            if seen[num] % k ==0:
                total += num*seen[num]
        return total