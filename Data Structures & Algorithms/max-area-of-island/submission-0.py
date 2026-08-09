class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0


        def dfs(row, col):

            if(row>=len(grid) or  row<0 or col >= len(grid[0]) or col<0):
                return
            if(grid[row][col]==0):
                return
            elif(grid[row][col]==1):
                nonlocal curr_area
                curr_area +=1
                
                grid[row][col]=0
            dfs(row-1, col)
            dfs(row+1, col)
            dfs(row, col-1)
            dfs(row, col+1)

        for j in range(len(grid[0])):
            for i in range(len(grid)):
                
                curr_area = 0
                if(grid[i][j]==1):
                    dfs(i,j)
                if(curr_area>max_area):
                    max_area=curr_area

        return max_area