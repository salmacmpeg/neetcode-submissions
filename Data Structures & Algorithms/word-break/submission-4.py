class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp ={}
        def rec(i):
            print("i: ", i,"i==len(s)", len(s))
            if i>=len(s):
                return 1
            if i>len(s):
                0
            if dp.get(i,-1) != -1:
                return dp[i]
            
            for wd in wordDict:
                j = len(wd)
                print("word ", wd)
                if j<= (len(s)) and wd == s[i:i+j]:
                    dp[i] = rec(i+j)
                    if dp[i] == 1 :
                        print("return 1")
                        return 1
            print("return 0")
            return 0
        
        x = rec(0)
        print("x is ", x)
        return True if x==1 else False