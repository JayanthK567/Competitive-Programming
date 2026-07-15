class Solution:
    def maximum69Number (self, num: int) -> int:
        word = str(num)
        word = word.replace("6","9",1)
        return int(word)