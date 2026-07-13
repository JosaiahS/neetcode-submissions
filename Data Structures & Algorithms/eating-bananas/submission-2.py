class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)
        res = high
         
        while low <= high:
            k = low + (high - low) // 2

            totalTime = 0
            for pile in piles:
                totalTime += math.ceil(float(pile) / k)
            
            if totalTime <= h:
                res = k
                high = k - 1
            else:
                low = k + 1
                
        return res