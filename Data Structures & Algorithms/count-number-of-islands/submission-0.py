class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0

        def explore(i, j):
            grid[i][j] = "0"

            if i + 1 < len(grid) and grid[i + 1][j] == "1":
                explore(i + 1, j)

            if i - 1 >= 0 and grid[i - 1][j] == "1":
                explore(i - 1, j)

            if j + 1 < len(grid[0]) and grid[i][j + 1] == "1":
                explore(i, j + 1)

            if j - 1 >= 0 and grid[i][j - 1] == "1":
                explore(i, j - 1)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    islands += 1
                    explore(i, j)

        return islands