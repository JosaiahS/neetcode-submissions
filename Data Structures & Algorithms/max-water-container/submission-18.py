class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxW = 0
        l,r = 0,len(heights)-1

        while l < r:
            maxW = max((r-l) * min(heights[l], heights[r]), maxW)
            if heights[l] < heights[r]:
                l +=1
            elif heights[r] < heights[l]:
                r -= 1
            else:
                l +=1
        return maxW