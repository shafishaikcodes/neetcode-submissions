class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        ans = []
        nums.sort()
        prev = None
        for i in range(len(nums)-2):
            if prev != None and prev == nums[i]:
                continue
            left, right = i+1, len(nums)-1
            while left < right:
                if nums[left] + nums[right] > -nums[i]:
                    right -= 1
                elif nums[left] + nums[right] == -nums[i]:
                    ans.append([nums[left], nums[right], nums[i]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                else:
                    left += 1
            prev = nums[i]
        return ans







