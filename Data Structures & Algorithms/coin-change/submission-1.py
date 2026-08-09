import sys
sys.setrecursionlimit(20000)

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        dp = {}

        def dfs(value):
            
            if(value<0):
                return float("inf")
            if(value == 0):
                return 0
            if(value in dp):
                return dp[value]
            best = float("inf")
            for i in coins:
                num_coins= dfs(value-i)
                best  = min(best, num_coins) 
            dp[value] = 1 + best
            return dp[value]
        num = dfs(amount)
        if(num == float("inf")):
            return -1

        return num