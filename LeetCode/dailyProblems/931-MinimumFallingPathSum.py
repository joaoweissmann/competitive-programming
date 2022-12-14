class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        mode = 2
        if (mode == 1): # mode == 1 -> brute force
            p = []
            best = 99999999
            for i, el in enumerate(matrix[0]):
                p.append((el, 0, (0, i)))
            while (p != []):
                x = p.pop()
                if (x[2][0] == len(matrix) - 1):
                    # is leaf
                    curr = x[0] + x[1]
                    if (curr < best):
                        best = curr
                else:
                    # isnt a leaf
                    p.append((matrix[x[2][0] + 1][x[2][1]], x[1] + x[0], (x[2][0] + 1, x[2][1])))
                    if ((x[2][1] - 1) >= 0):
                        p.append((matrix[x[2][0] + 1][x[2][1] - 1], x[1] + x[0], (x[2][0] + 1, x[2][1] - 1)))
                    if ((x[2][1] + 1) <= len(matrix) - 1):
                        p.append((matrix[x[2][0] + 1][x[2][1] + 1], x[1] + x[0], (x[2][0] + 1, x[2][1] + 1)))
        if (mode == 2): # mode == 2 -> dynamic programming
            dp = [[0 for i in range(len(matrix))] for i in range(len(matrix))]
            for i in range(len(matrix)):
                for j in range(len(matrix)):
                    if (i == 0):
                        dp[i][j] = matrix[i][j]
                    else:
                        if (j == 0):
                            dp[i][j] = min(matrix[i][j] + dp[i-1][j], matrix[i][j] + dp[i-1][j+1])
                        elif (j == len(matrix) - 1):
                            dp[i][j] = min(matrix[i][j] + dp[i-1][j], matrix[i][j] + dp[i-1][j-1])
                        else:
                            dp[i][j] = min(matrix[i][j] + dp[i-1][j], matrix[i][j] + dp[i-1][j-1], matrix[i][j] + dp[i-1][j+1])
            best = min(dp[len(matrix) - 1])
        return best
