class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [-1] * (len(nums)+1)
        def f(i):
            if dp[i] != -1:
                return dp[i]
            if i == len(nums)-1:
                return nums[i]
            if i > len(nums)-1:
                return 0
            dp[i] = max(nums[i] + f(i+2), f(i+1))
            return dp[i]
        return f(0)
