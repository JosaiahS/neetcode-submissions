class Solution:
    def isPalindrome(self, s: str) -> bool:
        l,r = 0, len(s) - 1

        while l < r:
            if not self.valid(s[l]):
                while not self.valid(s[l]) and l < r:
                    l += 1
            if not self.valid(s[r]):
                while not self.valid(s[r]) and l < r:
                    r -= 1
            
            if s[l].lower() != s[r].lower():
                return False
            
            l += 1
            r -= 1
        return True
            
    

    def valid(self, c):
        return (ord('a') <= ord(c) <= ord('z') or
                ord('A') <= ord(c) <= ord('Z') or
                ord('0') <= ord(c) <= ord('9'))