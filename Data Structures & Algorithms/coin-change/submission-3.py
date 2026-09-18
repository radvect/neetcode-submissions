import sys
sys.setrecursionlimit(20000)

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        number = 0 

        hash_tab = {}
        
        def dfs(left):
            
            if(left==0):
                return number
            if(left<0):
                return float('inf')

            if(left in hash_tab):
                return hash_tab[left]
            all_res = []
            for i in (coins):
                all_res.append(dfs(left-i))
            hash_tab[left] = 1+ min(all_res)
            return 1+  min(all_res)

        s = dfs(amount)
        print(hash_tab)
        if(s == float('inf')):
            return -1
        else:
            return s
        
        
        