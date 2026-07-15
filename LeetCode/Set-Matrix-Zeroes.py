class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        seenRow = set()
        seenCol = set()

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 0:
                    seenRow.add(row)
                    seenCol.add(col)

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if (row in seenRow) or (col in seenCol):
                    matrix[row][col] = 0