class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        complement = 0
        complements = {} #Key: num, Value: Index
        for i, num in enumerate(nums):
            complement = target - num
            if complement in complements:
                return [complements[complement], i]
            complements[num] = i
        