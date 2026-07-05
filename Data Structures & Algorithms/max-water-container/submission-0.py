class Solution:
    def maxArea(self, height: List[int]) -> int:
        i,j = 0, len(height)-1
        maxl,maxr,maxvol = 0, 0, 0
        while i<=j:
            maxl = height[i]
            maxr = height[j]
            maxvol = max(maxvol, (j-i) * min(maxl, maxr))
            if maxl<=maxr:
                i += 1
            else:
                j -= 1
        return maxvol
        