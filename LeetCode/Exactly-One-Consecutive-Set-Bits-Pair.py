class Solution:
    def consecutiveSetBits(self, n: int) -> bool:
        binary = format(n,'b')
        pair = False
        for i in range(len(binary)-1):
            if binary[i] == binary[i+1] and binary[i] == '1':
                if pair == True:
                    return False
                pair = True
        return pair
