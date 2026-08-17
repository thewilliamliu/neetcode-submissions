class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)
        
        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                    warmed = stack.pop()
                    result[warmed] = i - warmed
            stack.append(i)
        
        # Don't need the other branches. Always append, unless there is an increase in temp.

        return result