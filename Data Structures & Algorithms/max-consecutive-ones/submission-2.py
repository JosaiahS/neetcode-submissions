class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        curC = 0
        maxC = 0

        for num in nums:
            if num == 0:
                maxC = max(curC, maxC)
                curC = 0
            else:
                curC += 1
        maxC = max(curC,maxC)
        return maxC