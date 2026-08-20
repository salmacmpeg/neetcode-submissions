class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n==1:
            return nums[0]
        if n==2:
            return max(nums[n-2],nums[n-1])
        
        dpr=[0]*(n)
        dpr[n-1]=nums[n-1]
        dpr[n-2]= max(nums[n-2],nums[n-1])
        
        for i in range(n-3,0,-1):
            dpr[i]= max(nums[i]+dpr[i+2], dpr[i+1])

        dpl=[0]*(n)
        dpl[n-2]=nums[n-2]
        dpl[n-3]= max(nums[n-3],nums[n-2])
        
        for i in range(n-4,-1,-1):
            dpl[i]= max(nums[i]+dpl[i+2], dpl[i+1])

      
        return max(dpl[0], dpr[1])