class Solution:
    def maxArea(self, heights: List[int]) -> int:
        largest =0 
        l = len(heights)
        i =0
        j = l-1
        while i < j:
            miny = min(heights[i],heights[j])
            temp = miny*(j-i)
            largest = max(largest, temp)

            if heights[i]<= heights[j]:
                i+=1
            else:
                j-=1
           
        return largest