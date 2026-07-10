class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        if n == 0:
            return ""

        lans = 0
        rans = 0

        def expand(l: int, r: int) -> None:
            nonlocal lans, rans

            while l >= 0 and r < n and s[l] == s[r]:
                if r - l > rans - lans:
                    lans = l
                    rans = r

                l -= 1
                r += 1

        for i in range(n):
            expand(i, i)       # Odd length
            expand(i, i + 1)   # Even length

        return s[lans:rans + 1]