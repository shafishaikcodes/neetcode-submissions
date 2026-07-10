class Solution:
    def countSubstrings(self, s: str) -> int: 
        n = len(s)

        if n == 0:
            return 0
        count = 0

        def expand(l: int, r: int) -> None:
            nonlocal count

            while l >= 0 and r < n and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1

        for i in range(n):
            expand(i, i)       # Odd length
            expand(i, i + 1)   # Even length

        return count