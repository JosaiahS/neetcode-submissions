class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # index, height
        maxarea = 0

        for i, h in enumerate(heights):
            start= i
            while stack and stack[-1][1] > h:
                ind, height = stack.pop()
                maxarea = max(maxarea, height * (i - ind))
                start = ind
            stack.append((start, h))
        
        for i, h in stack:
            maxarea=max(maxarea, h * (len(heights) - i))
        return maxarea