class Solution:
    def getLeastFrequentDigit(self, n: int) -> int:
        seen = {}
        smallest = float('inf')
        qualify = set()
        while n > 0:
            current = n%10
            seen[current] = seen.get(current,0)+1
            n //=10
        for num in seen:
            if seen[num] < smallest:
                smallest = seen[num]
        for num in seen:
            if seen[num] == smallest:
                qualify.add(num)
        return min(qualify)