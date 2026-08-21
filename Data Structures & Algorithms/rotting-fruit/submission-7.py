# Edge case 1: find out if there are remaining fresh oranges.
# Edge case 2: if there were no fresh oranges to begin with, return 0.
# Minute count, increment within each queue number.

from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        minute = 0
        fresh = 0
        rotted = [[False] * len(grid[0]) for _ in range(len(grid))]
        
        q = deque()

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    rotted[r][c] = True
                    q.append((r, c, 0))
        
        while q:
            r, c, m = q.popleft()
            minute = max(minute, m)
            
            directions = [(1,0), (-1,0), (0,1), (0,-1)]

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                
                if (0 <= nr < len(grid) 
                and 0 <= nc < len(grid[0]) 
                and not rotted[nr][nc]
                and grid[nr][nc] == 1
                ):
                    rotted[nr][nc] = True
                    fresh -= 1
                    q.append((nr, nc, m+1))
        
        return minute if fresh == 0 else -1


                

        

        
        
        
        