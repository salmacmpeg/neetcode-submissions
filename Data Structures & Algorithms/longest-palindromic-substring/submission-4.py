class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(left,right):
            while left>=0 and right<len(s) and s[left]==s[right]:
                left-=1
                right+=1
            return s[left+1:right]
        max_len=1
        max_pal = s[0]
        
        for i in range(len(s)):
            temp = expand(i,i)
            # print(f"return odd expantion for {s[i]} is {temp}")        
            if len(temp)>max_len:
                max_len = len(temp)
                max_pal = temp

        for i in range(len(s)):
            temp = expand(i,i+1)        
            if len(temp)>max_len:
                max_len = len(temp)
                max_pal = temp
        return max_pal