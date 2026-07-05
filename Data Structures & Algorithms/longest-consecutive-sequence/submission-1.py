class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        set_s = set (nums)
        maximum = 0
        for i in nums:
            if i-1 in set_s:
                continue
            mx = 0
            while i+1 in set_s:
                mx += 1
                i += 1
                maximum = max(maximum, mx)
        return maximum + 1

        