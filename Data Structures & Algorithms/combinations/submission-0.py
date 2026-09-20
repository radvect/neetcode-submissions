class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        path = []        
        res = []

        available = [i for i in range(1,n+1)]
        used = [False for i in range(1,n+1)]

        def backtracking(start):
            if(len(path)==k):
                res.append(path.copy())
                return

            for i in range(start,len(available)):
                if(used[i] is True):
                    continue
                
                used[i]= True
                path.append(available[i])
                backtracking(i+1)
                path.pop()
                used[i] = False

        backtracking(0)

        return res