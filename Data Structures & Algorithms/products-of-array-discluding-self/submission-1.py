class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix, postfix = [1]*len(nums), [1]*len(nums)
        p1, p2 = 1, 1
        left, right = 1, len(nums)-2
        while left < len(nums) and right > -1:
            p1 *= nums[left-1]
            prefix[left] = p1
            p2 *= nums[right+1]
            postfix[right] = p2
            left += 1
            right -= 1
        ans = []
        for i in range(len(nums)):
            ans.append(prefix[i] * postfix[i])
        return ans


        