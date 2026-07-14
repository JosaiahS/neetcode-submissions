class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        curMax = 0
        maxOnes = 0

        for num in nums:
            if num == 0:
                maxOnes = max(maxOnes, curMax)
                curMax = 0
            else:
                curMax += 1
        
        maxOnes = max(maxOnes, curMax)

        return maxOnes