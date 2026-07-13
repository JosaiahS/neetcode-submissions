class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        bucket = [0] * 26

        for i in range(len(s)):
            bucket[ord('a') - ord(s[i])] += 1
            bucket[ord('a') - ord(t[i])] -= 1
        
        for val in bucket:
            if val != 0:
                return False
        return True