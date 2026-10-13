from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        def bfs(queue, fresh):
            
            minutes = 0
             
            while queue and fresh > 0:
                level_size = len(queue)
                for i in range(level_size):
                    curr_i, curr_j = queue.popleft()

                    for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                        ni = curr_i + di
                        nj = curr_j + dj

                        if (0 <= ni < len(grid)
                            and 0 <= nj < len(grid[0])
                            and grid[ni][nj] == 1):

                            grid[ni][nj] = 2
                            queue.append((ni, nj))
                            fresh -=1
                minutes+=1
            return minutes, fresh

        queue = deque([])
        fresh = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1
        
        mins, fresh = bfs(queue, fresh)

        if fresh==0:
            return mins
        else: 
            return -1