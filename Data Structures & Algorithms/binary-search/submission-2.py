class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = len(nums)
        left = 0 
        right = l-1
        while left <= right:
            mid = left + (right-left)//2
            if nums[mid] == target :
                return mid
            if nums[mid] > target:
                right = mid -1
            else :
                left = mid +1
        return -1
        