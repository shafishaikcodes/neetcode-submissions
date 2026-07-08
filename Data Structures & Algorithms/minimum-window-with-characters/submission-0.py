from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left, right = 0, 0
        count = 0
        ans = ""

        d_need = defaultdict(int)
        for char in t:
            d_need[char] += 1

        d_have = defaultdict(int)

        while left < len(s):
            if count == len(t):
                while s[left] not in d_need:
                    left += 1

                if ans == "":
                    ans = s[left:right]
                elif len(ans) > len(s[left:right]):
                    ans = s[left:right]

                if d_have[s[left]] <= d_need[s[left]]:
                    count -= 1

                d_have[s[left]] -= 1
                left += 1
                continue

            if right >= len(s):
                break

            if s[right] in d_need:
                if d_have[s[right]] < d_need[s[right]]:
                    count += 1

                d_have[s[right]] += 1
                right += 1
            else:
                right += 1

        return ans