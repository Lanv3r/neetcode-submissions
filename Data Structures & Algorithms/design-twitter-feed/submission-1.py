class Twitter:

    def __init__(self):
        self.tweets = []
        self.follows = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets.append((tweetId, userId))

    def getNewsFeed(self, userId: int) -> List[int]:
        authors = self.follows.get(userId, set()) | {userId}
        feed = []
        for i in range(len(self.tweets) -1, -1, -1):
            if self.tweets[i][1] in authors:
                feed.append(self.tweets[i][0])
                if len(feed) == 10:
                    break
        return feed



    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.follows:
            self.follows[followerId].add(followeeId)
        else:
            self.follows[followerId] = {followeeId}

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)
