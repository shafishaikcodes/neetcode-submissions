class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0

        while i < n:
            correct_index = nums[i]

            # n cannot be placed because index n does not exist
            if nums[i] < n and nums[i] != nums[correct_index]:
                nums[i], nums[correct_index] = nums[correct_index], nums[i]
            else:
                i += 1

        # The first number not at its correct index is missing
        for i in range(n):
            if nums[i] != i:
                return i

        return n