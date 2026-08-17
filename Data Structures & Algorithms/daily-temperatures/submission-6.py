class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)
        
        for i in range(len(temperatures)):

            if i == 0:
                stack.append(i)
        
            elif temperatures[i] <= temperatures[i-1]: 
                stack.append(i)
            else:
                while stack and temperatures[i] > temperatures[stack[-1]]:
                    warmed = stack.pop()
                    result[warmed] = i - warmed
                stack.append(i)

        return result