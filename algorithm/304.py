class NumMatrix:
    def __init__(self, matrix):  # powcai 智能缓存
        m = len(matrix)
        if m == 0:
            return
        n = len(matrix[0])
        if n == 0:
            return
        self.dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            tmp = 0
            for j in range(1, n + 1):
                tmp += matrix[i - 1][j - 1]
                self.dp[i][j] = tmp
        for j in range(1, n + 1):
            for i in range(1, m + 1):
                self.dp[i][j] += self.dp[i - 1][j]

        for i in range(m + 1):
            for j in range(n + 1):
                print('{0:3}'.format(self.dp[i][j], ' '), end=' ')  # 对齐输出
            print()

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.dp[row2 + 1][col2 + 1] - self.dp[row1][col2 + 1] - self.dp[row2 + 1][col1] + self.dp[row1][col1]


if __name__ == '__main__':
    matrix = [
        [3, 0, 1, 4, 2],
        [5, 6, 3, 2, 1],
        [1, 2, 0, 1, 5],
        [4, 1, 0, 1, 7],
        [1, 0, 3, 0, 5]
    ]
    obj = NumMatrix(matrix)
    print(obj.sumRegion(1, 1, 2, 2))
