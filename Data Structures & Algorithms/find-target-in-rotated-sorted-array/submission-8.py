class Solution:
    def bsearch(self, left, right, slist, tar):
        while left <= right:
            mid = left + (right-left)//2
            if tar == slist[mid]:
                return mid
            elif tar > slist[mid]:
                left= mid + 1
            else:
                right = mid - 1
        return -1
        
    def search(self, nums: List[int], target: int) -> int:
        kmin =0 
        kmax = len(nums)-1
        while kmin < kmax:
            kmid = kmin + (kmax - kmin)//2
            if nums[kmid] > nums[kmax]:
                kmin = kmid + 1
            elif nums[kmid] < nums[kmax]:
                kmax = kmid

        res = -1
        kmax = len(nums)-1
        if kmin <= kmax and target <= nums[kmax] and target >= nums[kmin]: 
            res = self.bsearch (kmin, kmax , nums, target)
        else:
            res = self.bsearch (0, kmin , nums, target)
        return res
       

