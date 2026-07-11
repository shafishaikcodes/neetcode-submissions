class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [-1] * (n + 1)
        res[0] = 0
        for i in range(1, n+1):
            if i % 2 == 1:
                res[i] = res[i-1] + 1
                continue
            count = 0
            num = i
            while num:
                count += 1
                num = num & (num - 1)
            res[i] = count
        return res
