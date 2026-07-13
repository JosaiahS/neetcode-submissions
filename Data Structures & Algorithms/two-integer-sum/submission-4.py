class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev = {}
        for i, n in enumerate(nums):
            complement = target - n
            if complement in prev:
                return [prev[complement], i]
            prev[n] = i