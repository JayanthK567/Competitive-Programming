class Solution:
    def maxFreqSum(self, s: str) -> int:
        seen = {}
        vowels = {'a','e','i','o','u'}
        maxVowel = 0
        maxCons = 0
        for ch in s:
            seen[ch] = seen.get(ch,0) + 1
        for ch in seen:
            if ch in vowels:
                maxVowel = max(maxVowel,seen[ch])
            else:
                maxCons = max(maxCons, seen[ch])
        return maxVowel + maxCons
