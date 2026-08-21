class Solution:
    def numDecodings(self, s: str) -> int:
        numd = 0
        n = len(s)
        if n==1:
            return int(s[0] != '0')
        
        counts = [0]*(n+1)
        counts[n]=1
        counts[n-1] = 1 if (s[n-1] in "123456789") else 0
        i = n-2
        while i>=0:
            if s[i]!='0':
                counts[i] += counts[i+1]
            if (s[i]=='1') or (i<n-1 and s[i]=='2' and s[i+1] in "0123456"):
                counts[i] += counts[i+2]
            i-=1
           


        return counts[0]