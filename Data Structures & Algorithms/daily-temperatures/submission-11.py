class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)
        s =[]
        for i , t in enumerate(temperatures):
            if len(s)==0 or t<= temperatures[s[-1]]:
                s.append(i)
            else:
                while len(s)>0 and t>temperatures[s[-1]]:
                    res[s[-1]]= i - s[-1]
                    s.pop()
                s.append(i)

        return res