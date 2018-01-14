from datetime import datetime

from mp3fromrss import Episode

class FeedReader():
    def __init__(self, feedSource):
        self.feedSource = feedSource

    def getNextEpisode(self):
        items = self.feedSource.run()

        for item in items:
            episode = self._parseItem(item)
            if episode != None:
                yield episode

    def _parseItem(self, item):
        links = item['links']

        if len(links) > 0:
            publishedDate = datetime.strptime(item['published'][:-6], '%a, %d %b %Y %H:%M:%S')
            return Episode(publishedDate, item['links'][0]['href'])

        return None
