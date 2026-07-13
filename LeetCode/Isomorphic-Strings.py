class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping = {}
        if len(set(s)) != len(set(t)):
            return False
        for i in range(len(s)):
            if s[i] in mapping and mapping[s[i]] != t[i]:
                return False
            mapping[s[i]] = t[i]
        return True