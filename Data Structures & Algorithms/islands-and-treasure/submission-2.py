from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque() ## Only need one BFS for multi-source.

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    q.append((r, c, 0))

        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        while q:
            r, c, dist = q.popleft()

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if (0 <= nr < len(grid)
                and 0 <= nc < len(grid[0])
                and grid[nr][nc] != -1
                and grid[nr][nc] != 0
                and dist+1 < grid[nr][nc]):
                    grid[nr][nc] = dist + 1 # One farther than origin.
                    q.append((nr, nc, dist + 1))
        