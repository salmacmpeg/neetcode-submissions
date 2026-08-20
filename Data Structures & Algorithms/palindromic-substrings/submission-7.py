class Solution:
    nums = 0
    def countSubstrings(self, s: str) -> int:
        
        def expand(left,right):
            while left>=0 and right<len(s) and s[left]==s[right]:
                left-=1
                right+=1
                self.nums+=1
        for i in range(len(s)):
            expand(i,i)
            expand(i,i+1)            
        # print(sset)
        return self.nums