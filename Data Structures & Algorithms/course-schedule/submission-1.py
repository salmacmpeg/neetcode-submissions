class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        hashy = defaultdict(set)
        for item in prerequisites:
            hashy[item[0]].add(item[1])
 
        # print(f'prerequisites: {prerequisites}')
        # print("hashy",hashy)

        def rec_dfs(i):
            listy = hashy[i]
            # print(f'i {i}, listy:{listy}, visited {visited}')
            while len(listy)>0:
                nextn = listy.pop()
                if visited[nextn]== True :
                    return False
                visited[nextn] = True
                if not rec_dfs(nextn):
                    return False
                visited[nextn] = False
            return True

        for i in range(numCourses):
            visited = [False]*numCourses
            visited[i]= True
            # print("calling from main with i:",i)
            if rec_dfs(i) == False:
                return False


        return True