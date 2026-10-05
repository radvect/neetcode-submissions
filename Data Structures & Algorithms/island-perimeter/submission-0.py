class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0
        visited = set()
        def dfs(i,j):
            nonlocal perimeter
            
            if i < 0 or j < 0 or j >= len(grid[0]) or i >= len(grid):
                perimeter += 1
                return
            if grid[i][j] == 0:
                perimeter += 1
                return
            if (i, j) in visited:
                return

            visited.add((i,j))
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)

            

        for i in range(len(grid)): 
            for j in range(len(grid[0])):
                if(grid[i][j]==1):
                    dfs(i,j)

        return perimeter