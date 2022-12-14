class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0 for x in nums]
        dp[0] = nums[0]
        for i, el in enumerate(nums):
            if (i == 0): 
                continue
            elif (i == 1):
                dp[i] = max(dp[i-1] - nums[i-1] + nums[i], dp[i-1])
            else:
                dp[i] = max(dp[i-1] - nums[i-1] + nums[i], dp[i-1], dp[i-2] + nums[i])
        return dp[-1]
