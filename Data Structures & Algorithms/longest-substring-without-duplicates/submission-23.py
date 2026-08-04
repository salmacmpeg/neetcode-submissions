class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        print(s)
        n = len(s)
        if n==0 or n==1:
            return n
        left=0
        right=0
        charset= set()
        while right < n :
            while left < n and s[right] in charset:
                charset.remove(s[left])
                left+=1
            charset.add(s[right])
            max_length = max(max_length, (right-left+1))
            right+=1

        return max_length