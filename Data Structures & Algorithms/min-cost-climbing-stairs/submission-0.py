class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        l = len(cost)
        if l<=2:
            return min(cost[0], cost[1])
        mincost = [0]* l
        mincost[l-1] = cost[l-1]
        mincost[l-2] = cost[l-2]
        for i in range(l-3,-1,-1):
            mincost[i] = cost[i] + min(mincost[i+1], mincost[i+2])
        return min(mincost[0], mincost[1])
