class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        lowered = s.lower()
        res = []

        for l in lowered:
            if l.isalnum() == True:
                res.append(l)
        
        n = len(res) - 1

        for i in range(n):
            if res[i] != res[n - i]:
                return False
        return True
        

