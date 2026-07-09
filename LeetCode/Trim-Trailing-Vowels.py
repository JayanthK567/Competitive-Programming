class Solution:
    def trimTrailingVowels(self, s: str) -> str:
        vowels = ('a','e','i','o','u')
        maxLen = len(s)-1
        while maxLen >= 0 and s[maxLen] in vowels:
            maxLen -= 1
        return s[0:maxLen+1]
