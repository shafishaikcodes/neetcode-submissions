from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left, right = 0, 0
        top_count, total_count = 0, 0
        ans = 0
        d = defaultdict(int)

        while right < len(s):
            d[s[right]] += 1
            total_count += 1

            if total_count - max(d.values()) <= k:
                ans = max(ans, right - left + 1)
            else:
                d[s[left]] -= 1
                total_count -= 1
                left += 1

            right += 1

        return ans