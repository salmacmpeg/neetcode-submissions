class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)
        n = len(s2)
        if n<k:
            return False
        left= 0
        right = left + k -1
        hash_s1 = {}
        hash_s2 = {}
        for i in range(k):
            hash_s1[s1[i]] = 1 + hash_s1.get(s1[i],0)
            hash_s2[s2[i]] = 1 + hash_s2.get(s2[i],0)

        while right < n and left +k-1 == right:
            if hash_s2 == hash_s1:
                return True
            right+=1
            if right< n: hash_s2[s2[right]] = 1 + hash_s2.get(s2[right],0)
            hash_s2[s2[left]]-=1
            if hash_s2[s2[left]] ==0:
                del hash_s2[s2[left]]
            left+=1

        return False
