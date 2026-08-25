class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp ={}
        def rec(i):
            if i>=len(s):
                return 1

            if dp.get(i,-1) != -1:
                return dp[i]
            
            for wd in wordDict:
                j = len(wd)
                if j<= (len(s)) and wd == s[i:i+j]:
                    dp[i] = rec(i+j)
                    if dp[i] == 1 :
                        return 1
            return 0
        
        x = rec(0)
        return True if x==1 else False