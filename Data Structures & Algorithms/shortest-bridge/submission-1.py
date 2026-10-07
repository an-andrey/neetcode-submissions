from collections import deque

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        seen = set()
        queue = deque()

        def dfs(i, j): 
            if (i, j) in seen or grid[i][j] != 1: 
                return 
            
            seen.add((i,j))
            queue.append((i,j,0))

            if i + 1 < n: 
                dfs(i+1, j)
            if i > 0: 
                dfs(i-1, j)
            if j + 1 < n: 
                dfs(i, j+1)
            if j > 0: 
                dfs(i, j-1)
        
        done = False
        for i in range(n): 
            if done: 
                break
            for j in range(n): 
                if grid[i][j] == 1: 
                    dfs(i, j)
                    done = True
                    break

        while queue: 
            r, c, dist = queue.popleft()

            for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                nr, nc = r+dr, c+dc

                if 0 <= nr < n and 0 <= nc < n and ((nr, nc)) not in seen: 
                    if grid[nr][nc] == 1: 
                        return dist

                    queue.append((nr, nc, dist+1))
                    seen.add((nr, nc))

        return 0

