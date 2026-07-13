class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for b in s:
            if b == "}":
                if stack and stack[-1] == "{":
                    stack.pop()
                    continue
                else:
                    return False
            if b == ")":
                if stack and stack[-1] == "(":
                    stack.pop()
                    continue
                else:
                    return False
            if b == "]":
                if stack and stack[-1] == "[":
                    stack.pop()
                    continue
                else:
                    return False
            stack.append(b)
        if stack:
            return False
        else:
            return True
