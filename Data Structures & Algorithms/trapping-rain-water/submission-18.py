class Solution:
    def trap(self, height: List[int]) -> int:
        l = len(height)
        Bucket = 0
        hashy = {}
        max_before = 0 
        for i in range(l):
            hashy[i] = [max_before,0]
            if height[i]>max_before:
                max_before = height[i]

        max_after = 0
        for i in range(l-1, -1, -1):
            hashy[i][1] =max_after
            if height[i]>max_after:
                max_after = height[i]

        for i in range(l):
            Bucket+= max(0, min(hashy[i][0], hashy[i][1]) - height[i])

        return Bucket





            