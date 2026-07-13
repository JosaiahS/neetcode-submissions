class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r = 0,1
        maxProfit = 0

        while l < r and r < len(prices):
            if prices[r] < prices[l]:
                l = r
                r += 1
            elif prices[r] > prices[l]:
                maxProfit = max(maxProfit, prices[r]-prices[l])
                r += 1
            else:
                l = r
                r += 1
        return maxProfit