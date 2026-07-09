class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def solve(arr):
            dp = [-1] * (len(arr) + 1)

            def f(i):
                if i > len(arr) - 1:
                    return 0

                if dp[i] != -1:
                    return dp[i]

                dp[i] = max(arr[i] + f(i + 2), f(i + 1))
                return dp[i]

            return f(0)

        list1, list2 = nums[:len(nums) - 1], nums[1:]

        return max(solve(list1), solve(list2))