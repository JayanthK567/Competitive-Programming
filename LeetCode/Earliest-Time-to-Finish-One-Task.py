class Solution:
    def earliestTime(self, tasks: List[List[int]]) -> int:
        shortest = 99999
        for task in tasks:
            shortest = min(sum(task),shortest)
        return shortest