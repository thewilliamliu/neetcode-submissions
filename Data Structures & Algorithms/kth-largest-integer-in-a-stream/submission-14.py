import heapq # Min-heap by default. Negate input/output for maxheap.

# Edge case: if you have less than k elements in your heap.
# Kth largest = use a min heap!

class KthLargest:

    # Always use self for instance variables.
    

    def __init__(self, k: int, nums: List[int]):
        self.k = k

        self.heap = []
        for i in nums:
            heapq.heappush(self.heap, i)
        if len(nums) - k > 0:
            for j in range(len(nums) - k):
                heapq.heappop(self.heap)
        
    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        
        if len(self.heap) > self.k:
            heapq.heappop(self.heap) # Get rid of k+1th element.
        
        return self.heap[0] # View smallest element in length k.
        
        
        
