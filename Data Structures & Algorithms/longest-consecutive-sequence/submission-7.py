class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)<1:
            return 0
        hashes = {}
        for n in nums:
            hashes[n]=1

        longest = 1
        for n in nums:
            if (n-1) not in hashes:
                hashes[n]=1 #possible start
                curr =n+1
                while curr in hashes:
                    hashes[n]+=1
                    curr+=1
                    if hashes[n] > longest:
                        longest =hashes[n]
        return longest