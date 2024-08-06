class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        if not matrix or not matrix[0]:
            return

        self.row = len(matrix)
        self.col = len(matrix[0])

        # Create a prefix sum matrix
        self.prefixSum = [[0] * (self.col + 1) for _ in range(self.row + 1)]

        for i in range(1, self.row + 1):
            for j in range(1, self.col + 1):
                self.prefixSum[i][j] = matrix[i - 1][j - 1] + \
                    self.prefixSum[i - 1][j] + self.prefixSum[i][j - 1] - self.prefixSum[i - 1][j - 1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # Calculate the sum of the region using the prefix sum matrix
        return self.prefixSum[row2 + 1][col2 + 1] - self.prefixSum[row2 + 1][col1] - self.prefixSum[row1][col2 + 1] + self.prefixSum[row1][col1]
