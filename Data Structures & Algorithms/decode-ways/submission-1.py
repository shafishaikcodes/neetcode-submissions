class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [-1] * (len(s) + 1)
        def f(index: int) -> int:
            if dp[index] != -1:
                return dp[index]
            if index == len(s):
                return 1
            if s[index] == "0":
                return 0
            left = f(index + 1)
            right = 0
            if index + 1 < len(s):
                number = int(s[index:index + 2])
                if 10 <= number <= 26:
                    right = f(index + 2)
            dp[index] = left + right

            return dp[index]

        return f(0)