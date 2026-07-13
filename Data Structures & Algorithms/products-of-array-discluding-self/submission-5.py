from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = self.brute_force_product(nums)
        return result
        
    def brute_force_product(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n  # Initialize the result list with 1s
        for i in range(n):
            for j in range(n):
                if i != j:
                    res[i] *= nums[j]  # Multiply the elements
        return res
