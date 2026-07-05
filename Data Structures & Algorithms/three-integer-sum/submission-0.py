class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()

        for i in range(len(nums)):
            seen = {}

            for j in range(i + 1, len(nums)):
                need = -(nums[i] + nums[j])

                if need in seen:
                    triplet = tuple(sorted([nums[i], nums[j], need]))
                    ans.add(triplet)

                seen[nums[j]] = 1

        return [list(x) for x in ans]