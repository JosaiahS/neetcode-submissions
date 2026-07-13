class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #initialize variables
        l, r = 0, len(heights) - 1
        res = 0

        #while loop conditions
        while l < r:
            #Calculating res by taking the max of res or the calculation of the minimum height multiplied by the width
            res = max(res, min(heights[l], heights[r]) * (r - l))
            #To attempt to maximize the area, we increment or decrement the column with the lower height 
            if heights[l] < heights[r]:
                l += 1
            elif heights[r] <= heights[l]:
                r -= 1
        #Return the integer     
        return res

    #Brute force way of solving this problem
    #Time O(n^2)
    #Space O(1)
    def maxAreaBruteForce(self, heights: List[int]) -> int:
        max_area = 0
        n = len(heights)
        for l in range(n):
            for r in range(l + 1, n):
                height = min(heights[l], heights[r])
                width = r - 1
                max_area = max(max_area, height * width)

        return max
