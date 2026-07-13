class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevmap = {}
        for i, num in enumerate(nums):
            complement=target-num
            if complement in prevmap:
                return [prevmap[complement],i]
            prevmap[num] = i