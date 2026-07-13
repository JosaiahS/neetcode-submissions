class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        #Creating a set allows us to remove duplicates
        numSet = set(nums)
        #To keep track of the longest streak of consecutive integers
        longest = 0

        for n in nums:
            #To check that it is a starting sequence, check if a left neightbor exists
            #If a left neighbor exist, then it is not a starting sequence
            if (n - 1) not in numSet:
                length = 0
                #We check how many consecutive integers exists from the start of the sequence
                while (n + length) in numSet:
                    #Increment length to continue to check for consecutive integers
                    length += 1
                #We choose the greatest value from either length or longest
                longest = max(length, longest)
        #return the greatest number of consecutive integers within the array.
        return longest 

