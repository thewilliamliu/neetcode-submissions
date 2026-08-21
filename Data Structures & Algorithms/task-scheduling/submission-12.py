import heapq
from collections import deque

## Items/values/keys all different.

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        heap = []
        freq = {}
        cooldown = deque()
        cycle = 0

        for task in tasks:
            ## Quick trick to add something that doesn't exist, or increment.
            freq[task] = freq.get(task,0) + 1 
        
        heap = [(-count, letter) for letter, count in freq.items()]  
        ## Create a tuple here.
        heapq.heapify(heap)

        while heap or cooldown:
            # Always check if the deque/heap is empty, just as you do with heap.
            if cooldown and cooldown[-1][0] == cycle: 
                _, count, letter = cooldown.pop()
                heapq.heappush(heap, (count, letter))

            if heap:
                count, letter = heapq.heappop(heap)
                count += 1
                if count != 0: cooldown.appendleft((cycle+n+1, count, letter))
            

            cycle += 1

        return cycle
