class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)

        left = 0
        currsum = nums[0]
        ans = nums[0]

        while left < n - 1:
            left += 1

            # Option 1: start a new subarray here
            startsum = nums[left]

            # Option 2: continue the previous subarray
            currsum += nums[left]

            # Starting here is better than continuing
            if currsum < startsum:
                currsum = startsum

            if currsum > ans:
                ans = currsum

        return ans