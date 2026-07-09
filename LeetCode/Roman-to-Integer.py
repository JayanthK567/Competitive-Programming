class Solution:
    def romanToInt(self, s: str) -> int:
        data = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }
        output = 0
        if len(s) == 1:
            return data[s]
        for i in range(0,len(s)-1):
            current = s[i]
            next_ = s[i+1]
            if data[current] < data[next_]:
                output -= data[current]
            else:
                output += data[current]
        output += data[next_]
        return output
