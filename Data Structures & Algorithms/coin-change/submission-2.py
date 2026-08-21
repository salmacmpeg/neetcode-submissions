class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp ={}
        def rec(m):
            # print("rec with m : ",m)
            if m==0:
                return 0
            if m<0:
                return 2**30
            if m in dp:
                return dp[m]
            min_num =2**30
            for coin in coins:
                res1 = 1+ rec(m-coin)
                min_num = min(res1, min_num)
            # print(f'at the end of loop with m {m}')
            dp[m]= int(min_num)
            return int(min_num)
        fres = rec(amount)
        if fres >= 2**30:
            return -1
        else:
            return int(fres)
