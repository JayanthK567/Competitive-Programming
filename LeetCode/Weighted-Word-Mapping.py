class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        # ord(a) = 97, ord(z) = 122
        output = ""
        for word in words:
            wordSum = 0
            for ch in word:
                index = ord(ch)-97
                wordSum += weights[index]
            value = wordSum%26
            output += chr(-(value-122))
        return output
