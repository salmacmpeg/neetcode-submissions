class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        hashy = defaultdict(set)
        degrees = {elem:0 for elem in range(numCourses)}
        for item in prerequisites:
            hashy[item[1]].add(item[0])
            degrees[item[0]]+=1
        
        min_heap = []
        for i in range(numCourses):
            heapq.heappush(min_heap, (degrees[i], i)) #be careful it is freq,node 
        # print(f'prerequisites: {prerequisites}')
        # print("hashy",hashy)
        # print("degrees",degrees)
        # print("heapq",min_heap)

        visited = 0
        while len(min_heap)>0:
            min_freq, min_node = heapq.heappop(min_heap)
            if min_freq>degrees[min_node]:
                continue
            if min_freq!= 0 :
                return False
            for elem in hashy[min_node]:
                degrees[elem]-=1
                heapq.heappush(min_heap,(degrees[elem],elem ))
            visited+=1

        return visited==numCourses