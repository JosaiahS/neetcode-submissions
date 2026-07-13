class Solution:
    def isValid(self, s: str) -> bool:
        
        if len(s) == 1:
            return False

        brackets = {'}':'{',']':'[',')':'('}
        stack = []

        for c in s:
            if c in brackets and len(stack) > 0:
                if stack[-1] == brackets[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if len(stack) == 0 else False
