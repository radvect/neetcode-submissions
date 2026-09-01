class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        pacific = set()
        atlantic = set()
        
        def dfs_pacific(i, j,value):
            # print(i,j)
            if(i == -1 or j == -1):
                #print(i,j)
                return True
            if(i == len(heights) or j == len(heights[0])):
                #print(i,j)
                return False
            if(heights[i][j]>value):
                # print(heights[i][j])
                # print(value)
                # print(i,j)
                return False    
            if((i,j) in visited):
                #print(i,j)
                return False
            visited.add((i,j))

            return dfs_pacific(i-1, j, heights[i][j]) or dfs_pacific(i+1, j,heights[i][j]) or dfs_pacific(i, j-1, heights[i][j]) or dfs_pacific(i, j+1, heights[i][j])


        def dfs_atlantic(i, j,value):
            if(i == len(heights) or j == len(heights[0])):
                return True
            if(i==-1 or j == -1):
                return False
            if(heights[i][j]>value):
                return False
            if((i,j) in visited):
                return False
            visited.add((i,j))
            
            
            return dfs_atlantic(i-1, j, heights[i][j]) or dfs_atlantic(i+1, j,heights[i][j]) or dfs_atlantic(i, j-1, heights[i][j]) or dfs_atlantic(i, j+1, heights[i][j])


        
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                visited = set()
                if(dfs_atlantic(i,j,10001)):
                    atlantic.add((i,j))
                visited = set()
                if(dfs_pacific(i,j,10001)):
                    pacific.add((i,j))
        
        print(sorted(pacific))
        # print(atlantic)
        return list(pacific & atlantic)