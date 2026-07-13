class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = []
    
        for i in range(n):
            multiply = 1
            for j in range(n):
                if i != j:
                    multiply *= nums[j]
            res.append(multiply)
        return res