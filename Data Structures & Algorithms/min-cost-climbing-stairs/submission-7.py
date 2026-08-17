class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        arr = [0] * (len(cost)+1) # Include the top here!
        
        for i in range(len(cost)+1):
            if i == 0:
                arr[i] = 0
            elif i == 1:
                arr[i] = 0
            else:
                arr[i] = min(cost[i-1]+arr[i-1], cost[i-2]+arr[i-2])
    
        return arr[len(cost)]

