class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perim = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])): 
                if grid[i][j] == 1:
                    if i > 0: 
                        if not grid[i-1][j]: 
                            perim += 1
                    else:
                        perim += 1
                    if j > 0: 
                        if not grid[i][j-1]: 
                            perim += 1
                    else: 
                        perim += 1

                    if i < len(grid)-1:
                        if not grid[i+1][j]: 
                            perim +=1 
                    else: 
                        perim +=1 
                    
                    if j < len(grid[0])-1: 
                        if not grid[i][j+1]:
                            perim +=1 
                    else:
                        perim += 1

        return perim
                        
                    