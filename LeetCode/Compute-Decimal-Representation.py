class Solution:
    def decimalRepresentation(self, n: int) -> List[int]:
        i = 1
        output = []
        while n > 0:
            current = (i*(n%10))
            if current != 0:
                output.append(current)
            n = n//10
            i *= 10
        return output[::-1]