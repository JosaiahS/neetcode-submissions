class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return False
        
        opentoclose = {']':'[', ')':'(', '}':'{'}
        stack = []

        for c in s:
            if c in opentoclose:
                if stack and stack[-1] == opentoclose[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False