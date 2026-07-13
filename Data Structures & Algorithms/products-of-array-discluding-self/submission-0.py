class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)
        res = []

        for i in range(n):
            multiply = 1
            for j in range(n):
                if i != j:
                    multiply *= nums[j]
                    print(f"This is the current multiplication: {multiply}")
                    print(f"This is nums[{j}]: {nums[j]}")
            res.append(multiply)
            print(f"Appending to result: {multiply}")
        
        return res