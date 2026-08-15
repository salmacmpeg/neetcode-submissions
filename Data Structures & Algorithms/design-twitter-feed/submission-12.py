class Twitter:

    def __init__(self):
        self.tweetmap = defaultdict(list)
        self.count = 0
        self.followmap = defaultdict(set)
    def postTweet(self, userId: int, tweetId: int) -> None:
        if len(self.tweetmap[userId]) == 10:
            self.tweetmap[userId].pop(0)
        self.tweetmap[userId].append((tweetId, self.count))
        self.count+=1
        # print(self.tweetmap)
    def getNewsFeed(self, userId: int) -> List[int]:
        maxheap =[]
        for (tweedid,ttime) in self.tweetmap[userId]:
            heapq.heappush(maxheap, (-ttime,tweedid))

        for folweeId in self.followmap[userId]:
            for (tweedid,ttime) in self.tweetmap[folweeId]:
                heapq.heappush(maxheap, (-ttime,tweedid))  
        res =[]
        i = 0
        while i<10 and len(maxheap)>0:
            res.append(heapq.heappop(maxheap)[1])
            i += 1
        # print("heap", maxheap)    
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followeeId not in self.followmap[followerId] and followeeId != followerId:
            self.followmap[followerId].add(followeeId)
        # print(self.followmap)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followmap[followerId].discard(followeeId)
        # print(self.followmap)