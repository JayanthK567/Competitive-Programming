class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        output = []
        for num in order:
            if num in friends:
                output.append(num)
        return output