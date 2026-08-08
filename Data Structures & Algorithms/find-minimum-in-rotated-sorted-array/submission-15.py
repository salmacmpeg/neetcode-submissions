class Solution:
    def findMin(self, nums: List[int]) -> int:
        kmin =0 
        kmax = len(nums)-1
        sel = max(nums)
        while kmin < kmax:
            kmid = kmin + (kmax - kmin)//2

            if nums[kmid] > nums[kmax] :
                kmin = kmid + 1
            elif nums[kmax] > nums[kmid]:
                sel = min(sel, nums[kmid])
                kmax= kmid
            

        return nums[kmin]