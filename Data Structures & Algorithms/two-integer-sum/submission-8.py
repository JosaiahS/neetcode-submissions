class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        count = {}
        
        complement = 0
        for i, num in enumerate(nums):
            complement = target - num
            if complement in count:
                return [count[complement], i]
            count[num] = i

# for loop: O(n), dictionary lookup O(1). O(n) + O(1) = Runtime O(n)
# count worst case O(n). Memory O(n)
        