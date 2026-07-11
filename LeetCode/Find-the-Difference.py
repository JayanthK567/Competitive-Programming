class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        seen = {}
        for ch in s:
            seen[ch] = seen.get(ch,0)+1
        for ch in t:
            seen[ch] = seen.get(ch,0)-1
        for val in seen:
            if seen[val] != 0:
                return val
        return ""