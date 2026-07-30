class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashy = defaultdict(list)
        for i, _ in enumerate(strs):
            mystr = strs[i]
            count_arr = [0]*26
            for ch in mystr:
                count_arr[ord(ch) - ord('a')]+=1
            
            
            hashy[tuple(count_arr)].append(strs[i])

        return list(hashy.values())