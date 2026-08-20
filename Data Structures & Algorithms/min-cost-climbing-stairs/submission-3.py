class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        l = len(cost)
        if l<=2:
            return min(cost[0], cost[1])

        prev2 = cost[l-2]
        prev1 = cost[l-1]
        for i in range(l-3,-1,-1):
            curr = cost[i] + min(prev2,prev1)
            prev2,prev1 = curr, prev2
        return min(prev2,prev1)
