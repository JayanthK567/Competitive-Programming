class Solution:
    def vowelConsonantScore(self, s: str) -> int:
        vowels = {'a','e','i','o','u'}
        vc = 0
        cc = 0
        for ch in s:
            if ch.isalpha():
                if ch in vowels:
                    vc += 1
                else:
                    cc+= 1
        if cc == 0 or vc == 0:
            return 0
        else:
            return vc//cc