class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0,1
        maxp = 0
        while right < len(prices):
            if prices[left] < prices[right]:
                maxp = max(maxp, - prices[left] + prices[right] )
                right += 1
                continue
            left = right
            right += 1
        return maxp


        