class Solution:
    def isPalindrome(self, s: str) -> bool:
        i,j = 0, len(s) - 1

        while i < j:
            if not self.english(s[i]):
                while i < j and not self.english(s[i]):
                    i += 1
            if not self.english(s[j]):
                while j > i and not self.english(s[j]):
                    j -= 1
            
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        return True
    

    def english(self, c):
        return (ord('a') <= ord(c) <= ord('z') or
                ord('A') <= ord(c) <= ord('Z') or
                ord('0') <= ord(c) <= ord('9'))
