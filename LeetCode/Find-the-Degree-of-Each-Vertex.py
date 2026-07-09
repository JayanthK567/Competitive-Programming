class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        output = []
        for vert in matrix:
            output.append(sum(vert))
        return output