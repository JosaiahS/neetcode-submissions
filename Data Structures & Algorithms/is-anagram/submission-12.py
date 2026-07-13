class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        freq = [0] * 26  

        for i in range(len(s)):
            freq[ord(s[i]) - ord('a')] += 1
            freq[ord(t[i]) - ord('a')] -= 1
        
        for num in freq:
            if num != 0:
                return False
        return True
            
# Runtime: O(m + n) m being length of s and n being length of t
# Memory O(1). O(26) -> O(1)