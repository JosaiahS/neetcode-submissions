class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #Setting up two pointers
        l, r = 0, 1
        #Will hold the result
        maxP = 0

        #Loop until the right pointer reaches the end
        while r < len(prices):
            #Possible Profit
            if prices[l] < prices[r]:
                #Calculate profit
                profit = prices[r] - prices[l]
                #Assign maxP to hold the better profit
                maxP = max(maxP, profit)
            else:
                #We found the lowest price yet
                l = r
            #Increment r
            r += 1
        return maxP