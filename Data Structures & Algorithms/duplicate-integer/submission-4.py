class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if (len(nums) == 0 or len(nums) == 1):
            return False
        duplicate = set()
        for num in nums:
            if num in duplicate:
                return True
            duplicate.add(num)
        return False  