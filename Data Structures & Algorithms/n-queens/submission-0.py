class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        occupied_cols = set()
        diag1 = set()
        diag2 = set()
        path = []
        res = []

        queen = []


        # def diagonal_1(row, col, n):
        #     nonlocal diag1
        #     iter1 = 0 
        #     while row<n and col<n:
        #         diag1.add((row, col))
        #         row+=1
        #         col+=1
        #         iter1+=1
        #     return iter1
            

                
        
        # def diagonal_2(row, col, n):
        #     nonlocal diag2
        #     iter1  = 0
        #     while row<n and col>=0:
        #         diag2.add((row, col))
        #         row+=1
        #         col-=1
        #         iter1+=1
        #     return iter1

        def backtracking(row):
            nonlocal queen
            
            if(row==n):
                res.append(queen.copy())
                return

            for j in range(n):
                if(j in occupied_cols or row-j in diag2 or row+j in diag1):
                    continue
                else:
                    occupied_cols.add(j)
                    diag1.add(j+row)
                    diag2.add(row-j)
                    string_q = "."*n
                    string_q=string_q[:j] + "Q" + string_q[j+1:]
                    queen.append(string_q)
                    backtracking(row+1)
                    queen.pop()
                    occupied_cols.remove(j)
                    diag1.remove(j+row)
                    diag2.remove(row-j)


        backtracking(0)

        return res