class Twitter:

    def __init__(self):
        self.tweets = {}
        self.follows = {}
        self.count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.count += 1
        if userId not in self.tweets:
            self.tweets[userId] = []
        self.tweets[userId].append((self.count, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        authors = self.follows.get(userId, set()) | {userId}
        candidates = []
        for a in authors:
            if a in self.tweets:
                candidates.extend(self.tweets[a])
        
        candidates.sort(key=lambda x: x[0], reverse=True)
        return [tweetId for count, tweetId in candidates[:10]]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.follows:
            self.follows[followerId] = set()
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.follows and followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)
