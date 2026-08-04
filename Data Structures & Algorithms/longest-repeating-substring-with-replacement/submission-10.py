class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_hash={}
        n = len(s)
        max_freq=0
        max_len = 0
        if n==0:
            return 0
        right = left =0
        while right <n:
            char_hash[s[right]] = 1+ char_hash.get(s[right],0)
            max_freq = max(char_hash.values())
            right+=1

            if left<right and (((right-left)-max_freq) > k):
                char_hash[s[left]] -=1
                # max_freq = max(char_hash.values())
                left+=1
            
            max_len = max(max_len, (right-left))

        return max_len



