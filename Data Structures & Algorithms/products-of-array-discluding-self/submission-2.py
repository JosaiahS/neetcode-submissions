class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        n = len(nums)
        pre = 1
        post = 1

        for i in range(n):
            
            output.append(pre)
            #print(f"Iteration: {i}")
            #print(f"Current output: {output}")
            #print(f"pre: {pre}")
            #print(f"nums: {nums[i]}")
            pre *= nums[i]
            #print(f"pre: {pre}")
        for i in range(n-1,-1,-1):
            print(f"Post: {post}")
            print(f"Output[i]: {output[i]}")
            output[i] *= post
            print(f"Output[i] * post = {output[i]}")
            post *= nums[i]
            print(f"Post * nums[i] = {post}")
            print(f"Output: {output}")
        return output    
            
            