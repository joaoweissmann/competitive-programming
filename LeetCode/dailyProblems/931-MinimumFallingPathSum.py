class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
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
        return best
