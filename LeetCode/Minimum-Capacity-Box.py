class Solution:
    def minimumIndex(self, capacity: list[int], itemSize: int) -> int:
        lowest = 999
        table = {}
        for i in range(0,len(capacity)):
            if capacity[i] >= itemSize and capacity[i] not in table:
                lowest = min(lowest,capacity[i])
                table[capacity[i]] = i
        if lowest == 999:
            return -1
        else:
            return table[lowest]