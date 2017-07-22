import feedparser
from mp3fromrss import Mp3FromRSSDownloader
from mp3fromrss import FindAndDownloadMissing
from mp3fromrss import DownloadedEpisodesManager

class SGTTU(FindAndDownloadMissing):
    def __init__(self, logger, path):
        FindAndDownloadMissing.__init__(
            self,
            logger,
            DownloadedEpisodesManager(path),
            SGTTUDownloader(logger)
        )

    def _getName(self):
        return "SGTTU"

class SGTTUDownloader(Mp3FromRSSDownloader):
    MainRSSLink = 'http://www.theskepticsguide.org/feed/rss.aspx'
    DownloadServerDirectory = 'http://media.libsyn.com/media/skepticsguide/'

    def _getNextEpisode(self):
        feed = feedparser.parse(self.MainRSSLink)
        items = feed['items']

        for item in items:
            link = item['links'][0]['href']
            yield link

    def _findAllNewEpisodes(self, lastDownloadedEpisode):
        results = []
        for link in self._getNextEpisode():
            if lastDownloadedEpisode in link:
                return results

            results.append(link)

        return results

    def _createForLink(self, link):
        return link[len(self.DownloadServerDirectory):]

