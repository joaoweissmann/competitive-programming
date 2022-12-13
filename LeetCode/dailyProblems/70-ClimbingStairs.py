class Solution:
    def climbStairs(self, n: int) -> int:
        import math
        x = int(n/2)
        result = 0
        for i in range(x + 1):
            k = n - i
            result += math.comb(k,i)
        return result