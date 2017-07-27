import feedparser
import datetime

from mp3fromrss import Mp3FromRSSDownloader
from mp3fromrss import FindAndDownloadMissing
from mp3fromrss import DownloadedEpisodesManager

class Niezatapialni(FindAndDownloadMissing):
    def __init__(self, logger, path):
        FindAndDownloadMissing.__init__(
            self,
            logger,
            DownloadedEpisodesManager(path),
            NiezatapialniDownloader(logger)
        )

    def _getName(self):
        return "Niezatapialni"

class NiezatapialniDownloader(Mp3FromRSSDownloader):
    MainRSSLink = 'http://niezatapialni.com/?feed=rss2'
    DownloadServerDirectory = 'http://www.niezatapialni.com/podcast/'
    FilePrefixSize = 11 # File has additional prefix: '[YYYYMMDD] '

    def _getNextEpisode(self):
        feed = feedparser.parse(self.MainRSSLink)
        items = feed['items']
        for item in items:
            links = item['links']
            if (len(links) > 1):
                yield item['links'][1]['href']

    def _findAllNewEpisodes(self, lastDownloadedEpisode):
        cleanEpisodeName = lastDownloadedEpisode[self.FilePrefixSize:].lower()

        results = []
        for link in self._getNextEpisode():
            href = link.lower()
            if cleanEpisodeName in href:
                return results

            results.append(link)

        return results

    def _createForLink(self, link):
        onlyFileName = link.rpartition('/')[-1]
        return '[%s] %s' % (datetime.datetime.now().strftime('%Y%m%d'), onlyFileName)

