class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)
        ans = []
        kcopy = k
        for i in nums:
            d[i] += 1
        lis = [[] for _ in range(len(nums) + 1)]
        for key, val in d.items():
            lis[val].append(key)
        i = len(lis)-1
        while k > 0:
            k -= len(lis[i])
            ans.extend(lis[i])
            i -= 1
        return ans[:kcopy+1]

