from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.data = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.data[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        
        vals = self.data[key]
        left = 0
        right = len(vals) - 1
        res_ts = 0
        res_val = '' 
        while left <= right :
            mid = left + (right - left)//2
            if vals[mid][0] == timestamp:
                return vals[mid][1]
            elif vals[mid][0] > timestamp :
                right = mid - 1
            else:
                res_val = vals[mid][1]
                res_ts = timestamp
                left = mid + 1
        
        return res_val
