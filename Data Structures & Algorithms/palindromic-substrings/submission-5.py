class Solution:
    def countSubstrings(self, s: str) -> int:
        nums = 0
        sset = []
        def expand(left,right):
            while left>=0 and right<len(s) and s[left]==s[right]:
                left-=1
                right+=1
                sset.append(s[left+1:right])
        for i in range(len(s)):
            expand(i,i)
            expand(i,i+1)            
        # print(sset)
        return len(sset)