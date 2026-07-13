class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary = {}

        for i,n in enumerate(nums):
            complement = target - n
            if complement in dictionary:
                return ([dictionary[complement], i])
            else:
                dictionary[n] = i 
        
