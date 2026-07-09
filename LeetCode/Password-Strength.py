class Solution:
    def passwordStrength(self, password: str) -> int:
        score = 0
        changed = set(password)
        for ch in changed:
            if ch.islower():
                score += 1
            elif ch.isupper():
                score += 2
            elif ch.isdigit():
                score += 3
            else:
                score += 5
        return score