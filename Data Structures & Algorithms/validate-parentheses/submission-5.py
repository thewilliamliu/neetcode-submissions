class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for i, x in enumerate(s):
            if x == '(' or x == '{' or x == '[':
                stack.append(x)

            if (x == ')' or x == '}' or x == ']') and not stack:
                return False

            if x == ')':
                if stack[-1] == '(':
                    stack.pop()
                else:
                    return False

            if x == ']':
                if stack[-1] == '[':
                    stack.pop()
                else:
                    return False
            
            if x == '}':
                if stack[-1] == '{':
                    stack.pop()
                else:
                    return False
            
        return not stack