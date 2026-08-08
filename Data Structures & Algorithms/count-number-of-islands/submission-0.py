class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def dfs(row, col):
            if(row>=len(grid) or  row<0 or col >= len(grid[0]) or col<0):
                return
            if(grid[row][col]=="1"):
                grid[row][col]="0"
            elif(grid[row][col]=="0"):
                return
            dfs(row-1, col)
            dfs(row+1, col)
            dfs(row, col-1)
            dfs(row, col+1)
        num = 0
        for j in range(len(grid[0])):
            for i in range(len(grid)):
                if(grid[i][j]=="1"):
                    num+=1
                    dfs(i,j)

        return num