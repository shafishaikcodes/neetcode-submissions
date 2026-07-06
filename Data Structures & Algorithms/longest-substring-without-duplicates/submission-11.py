class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        left, right = 0, 1
        maxl = 1
        d = {}
        d[s[left]] = left
        while right < len(s):
            if s[right] in d:
                maxl = max(maxl, right - left)
                print(maxl)
                left = max(left, d[s[right]] + 1)
                d[s[right]] = right
                right += 1
                continue
            d[s[right]] = right
            right += 1
        return max(maxl, right - left)



        