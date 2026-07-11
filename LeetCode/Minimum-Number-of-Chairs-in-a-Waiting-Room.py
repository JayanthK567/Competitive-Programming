class Solution:
    def minimumChairs(self, s: str) -> int:
        chair = 0
        output = 0
        for ch in s:
            if ch == "E":
                chair += 1
            else: 
                chair -= 1
            output = max(output,chair)
        return output