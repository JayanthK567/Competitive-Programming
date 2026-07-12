class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        ordered = sorted(list(set(arr)))
        rank_map = {num: i + 1 for i, num in enumerate(ordered)}
        output = []
        for i in range(len(arr)):
            output.append(rank_map[arr[i]])
        return output