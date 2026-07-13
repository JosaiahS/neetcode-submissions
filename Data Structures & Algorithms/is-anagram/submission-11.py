class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        freq = [0] * 26

        for i in range(len(s)):
            freq[ord(s[i])-ord('a')] +=1
            freq[ord(t[i])-ord('a')] -=1
        
        for s in freq:
            if s != 0:
                return False
        return True
    
    # 2 for loops: 2O(n) = O(n). Runtime O(n + m)
    # array of length 26 O(26) = O(1). Memory O(1)