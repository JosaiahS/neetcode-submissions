class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        end = len(prices)
        l, r = 0, 1
        while l < r and r != end:
            if prices[l] > prices[r]:
                l = r
                r += 1
                continue
            elif prices[l] < prices[r]:
                maxP = max(maxP, prices[r] - prices[l])
                r += 1
            elif prices[l] == prices[r]:
                l = r
                r += 1
        return maxP