class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        deck = [i for i in range(1,maxPts+1)]
        if k == 0:
            return 1.0
        dp = []
        dp.append(1.0)
        window = 1.0 
        value = 0
        for i in range(1, k+maxPts):
            dp.append(window / maxPts)
            if i < k:
                window += dp[i]
            if i - maxPts >= 0 and i - maxPts < k:
                 window -= dp[i - maxPts]
        return sum(dp[k : min(n, k - 1 + maxPts) + 1])