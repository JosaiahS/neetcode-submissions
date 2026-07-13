class Solution:
    def isValid(self, s: str) -> bool:
        dictionary = {')': '(', ']': '[', '}': '{'}
        stack = []

        for c in s:
            if stack and c in dictionary:
                if dictionary[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False
            