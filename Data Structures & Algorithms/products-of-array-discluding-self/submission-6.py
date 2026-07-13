class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #This problem can be solved in O(n) by not using a nested loop
        #Find the prefix and put it into the res array
        #Then find the postfix and multiply it with respective indexes in res array
        
        
        #Creating [1,1,1,1] using [1] and the length of the nums array
        res = [1] * (len(nums))
        
        #Initializing prefix variable
        prefix = 1
        #Loop to find prefixes
        for i in range(len(nums)):
            #Making res[i] equal to the found prefix of the last for loop iteration
            res[i] = prefix
            #Multiplying the current prefix with the value at nums[i]
            prefix *= nums[i]
        #Initializing postfix variable
        postfix = 1
        #Making the for loop go in reverse for postfix
        #for i in range(length of array, the index we want to stop at, go in reverse)
        for i in range(len(nums)-1,-1,-1):
            #Multiplying the value at res[i] with the current postfix
            res[i] *= postfix
            #Multiplying the postfix with the value at index nums[i]
            postfix *= nums[i]
        #Returning the res array 
        return res    



    def brute_force_product(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n  # Initialize the result list with 1s
        for i in range(n):
            for j in range(n):
                if i != j:
                    res[i] *= nums[j]  # Multiply the elements
        return res    
            