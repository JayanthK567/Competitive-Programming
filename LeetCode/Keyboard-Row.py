class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first = "qwertyuiop"
        second = "asdfghjkl"
        third = "zxcvbnm"
        output = []
        for word in words:
            letters = word.lower()
            if set(letters) <= set(first) or set(letters) <= set(second) or set(letters) <= set(third):
                output.append(word)
        return output