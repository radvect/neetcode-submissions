class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        stairs_cost = [0]*(n+1)
        stairs_cost[0], stairs_cost[1] = cost[0], cost[1]

        for i in range(2, n):
            stairs_cost[i] = min(stairs_cost[i-1], stairs_cost[i-2]) + cost[i]
        stairs_cost[n] =  min(stairs_cost[n-1], stairs_cost[n-2])
        return stairs_cost[-1]