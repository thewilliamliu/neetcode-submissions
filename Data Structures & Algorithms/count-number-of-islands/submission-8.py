from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0

        marked = [[False] * len(grid[0]) for _ in range(len(grid))]

        for row in range(len(grid)):
            for col in range(len(grid[0])): 
                if grid[row][col] == "1" and marked[row][col] == False: # Grid contains strings!
                    islands += 1
                    marked[row][col] = True

                    q = deque()
                    q.append((row, col)) # Add a tuple, not just one object.

                    while q:
                        r, c = q.popleft()

                        directions = [(0,1), (0,-1), (1,0), (-1,0)]

                        for dr, dc in directions:
                            nr = r + dr
                            nc = c + dc

                            if (0 <= nr < len(grid) 
                            and 0 <= nc < len(grid[0]) 
                            and marked[nr][nc] == False 
                            and grid[nr][nc] == "1"): 
                                q.append((nr, nc))
                                marked[nr][nc] = True
        return islands
            

                    
                
            
        