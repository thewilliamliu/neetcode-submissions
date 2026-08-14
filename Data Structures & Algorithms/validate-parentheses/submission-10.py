class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        ## You can declare a hash map like this. Need commas.
        pairs = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for x in s:
            if x == '(' or x == '{' or x == '[':
                stack.append(x)

            if (x == ')' or x == '}' or x == ']') and not stack:
                return False

            if x in pairs and pairs[x] != stack[-1]:
                return False
            elif x in pairs:
                stack.pop()
            
        return not stack