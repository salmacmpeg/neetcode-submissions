class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        min_prev = nums[0]
        max_prev = nums[0]
        # print(f'min_prev: {min_prev}')
        # print(f'max_prev: {max_prev}')
        max_found= nums[0]
        for i in range(1,len(nums),1):
            r1 = nums[i]
            r2 = min_prev*nums[i]
            r3= max_prev*nums[i]

            max_prev =max(r1,r2,r3)
            min_prev = min(r1,r2,r3)
            # print(f'min_prev: {min_prev}')
            # print(f'max_prev: {max_prev}')
            max_found =max(max_found,max_prev)
       
        return (max_found)
