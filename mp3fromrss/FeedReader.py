from datetime import datetime

from mp3fromrss import Episode

class FeedReader():
    def __init__(self, feedSource):
        self.feedSource = feedSource

    def getNextEpisode(self):
        items = self.feedSource.run()

        for item in items:
            publishedDate = datetime.strptime(item['published'][:-6], '%a, %d %b %Y %H:%M:%S')
            for link in item['links']:
                if 'mp3' in link['href']:
                    yield Episode(publishedDate, link['href'])
