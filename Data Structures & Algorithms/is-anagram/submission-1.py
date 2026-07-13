class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        SHash, THash = {}, {}

        for i in range(len(s)):
            SHash[s[i]] = 1 + SHash.get(s[i], 0)
            THash[t[i]] = 1 + THash.get(t[i], 0)
        
        return SHash == THash
