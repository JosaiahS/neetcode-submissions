class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #define an empty set
        charSet = set()
        #left pointer
        l = 0
        #result
        res = 0

        for r in range(len(s)):
            #If the character we are at is already in the set, we enter the while loop
            while s[r] in charSet:
                #Characters at the beginning of the substring are removed from the set
                charSet.remove(s[l])
                #Left pointer is incremented. 
                #This action also shortens the substring 
                l += 1
            #While they are no duplicates in the set, we continue to loop normally and add characters to the set
            charSet.add(s[r])
            #During the for loop, res is constantly updated with the longest substring we find
            res = max(res, r - l + 1)
        #return the size of the longest substring that was found 
        return res
