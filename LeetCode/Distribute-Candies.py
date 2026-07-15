class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        limit = len(candyType)//2
        available = set(candyType)
        return min(limit,len(available))
