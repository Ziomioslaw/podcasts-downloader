class FeedReader():
    def __init__(self, episodes):
        self.episodes = episodes

    def getNextEpisode(self):
        for episode in self.episodes:
            yield episode
