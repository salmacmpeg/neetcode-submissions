class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashy = {}
        for elem in nums:
            hashy[elem]=(hashy.get(elem,0)+1)

        arr = []
        for elem, fre in hashy.items():
            arr.append([fre,elem])
        arr.sort()

        final_list = []
        i =0 
        while i<k:
            final_list.append(arr.pop()[1])
            i+=1
        return final_list
        