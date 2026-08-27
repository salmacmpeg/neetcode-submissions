class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sumall = sum(nums)
        if sumall%2!=0:
            return False
        half_sum = sumall/2
        n = len(nums)
        hasy={}
        def rec(i, csum):
            if csum > half_sum or i>=len(nums):
                return False
            if csum == half_sum:
                return True
            if hasy.get((i,csum),None) != None:
                return hasy[(i,csum)]
            donot = rec(i+1,csum )
            dotake = False
            if i+1 <= len(nums) -1:
                dotake = rec(i+1,csum+nums[i+1] )
            hasy[(i,csum)]= donot or dotake
            return donot or dotake
          
        return rec(0,nums[0]) 


