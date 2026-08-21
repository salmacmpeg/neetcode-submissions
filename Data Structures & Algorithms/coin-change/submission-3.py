class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp =[2**32]*(amount+1)
        dp[0] = 0
        for m in range(0,amount+1,1):
            min_amount = dp[m]
            for coin in coins:
                if m-coin <0:
                    continue
                else:
                    min_amount = min(min_amount, 1+dp[m-coin])
            dp[m] = min_amount
        
        if dp[amount] >= 2**30:
            return -1
        else:
            return dp[amount]