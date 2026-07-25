class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dictionary = {')':'(', ']':'[', '}':'{'}

        for c in s:
            if c in dictionary:
                if stack and dictionary[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return False if stack else True