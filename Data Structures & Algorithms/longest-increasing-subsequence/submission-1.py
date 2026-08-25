class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lsq= {}
        n= len(nums)-1
        lsq[nums[n]] = 1
        # print("lsq",lsq)
        all_max = 1  
        for i in range(n-1, -1, -1):
            max_set = 0
            elem = nums[i]
            # print("lsq",lsq)
            for key, val in lsq.items():
                if key > elem:
                    max_set =  max(max_set, val)
            lsq[elem] = 1+max_set
            all_max = max(all_max, 1+max_set)
        return all_max