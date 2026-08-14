# Convert to integers using int(x). Make sure you compare all the right types.

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for x in tokens:
            # Quicker than comparing using ands for each char.
            if x in "+-*/" and len(stack) > 1:
                if x == '+':
                    stack.append(int(stack.pop()) + int(stack.pop()))
                
                if x == '-':
                    # Order matters here!
                    last = int(stack.pop())
                    first = int(stack.pop())
                    stack.append(first-last)

                if x == '*':
                    stack.append(int(stack.pop()) * int(stack.pop()))

                if x == '/':
                    last = int(stack.pop())
                    first = int(stack.pop())
                    stack.append(first/last)
            else:
                stack.append(x)

        return int(stack.pop())