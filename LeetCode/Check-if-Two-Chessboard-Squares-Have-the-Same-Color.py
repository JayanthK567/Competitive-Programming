class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        data = {
            'a' : 1,
            'b' : 0,
            'c' : 1,
            'd' : 0,
            'e' : 1,
            'f' : 0,
            'g' : 1,
            'h' : 0
        }
        value1 = (data[coordinate1[0]] + int(coordinate1[1]))%2
        value2 = (data[coordinate2[0]] + int(coordinate2[1]))%2
        return value1 == value2