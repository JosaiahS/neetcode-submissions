class Solution:
    def isValid(self, s: str) -> bool:
        
        if len(s) == 1:
            return False

        brackets = {'}':'{',']':'[',')':'('}
        # Memory: O(n)
        stack = []

        # Runtime: O(n)
        for c in s:
            if c in brackets:
                if stack and stack[-1] == brackets[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False
