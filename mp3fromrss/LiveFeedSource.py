import feedparser

class LiveFeedSource():
    def __init__(self, rsslink):
        self.rsslink = rsslink

    def run(self):
        feed = feedparser.parse(self.rsslink)
        items = feed['items']

        return items
