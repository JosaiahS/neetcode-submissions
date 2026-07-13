class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i,o in enumerate(nums):
            for j,p in enumerate(nums):
                if i != j and o == p:
                    return True
        return False