class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevHash = {}
        for i,n in enumerate(nums):
            complement = target - n
            if complement in prevHash:
                return [prevHash[complement], i]
            prevHash[n] = i        