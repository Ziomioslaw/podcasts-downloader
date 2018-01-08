import feedparser
from datetime import datetime

from mp3fromrss import Mp3FromRSSDownloader
from mp3fromrss import FindAndDownloadMissing
from mp3fromrss import DownloadedEpisodesManager
from mp3fromrss import Downloader
from mp3fromrss import Episode

class Niezatapialni(FindAndDownloadMissing):
    def __init__(self, logger, path):
        FindAndDownloadMissing.__init__(
            self,
            logger,
            DownloadedEpisodesManager(path),
            NiezatapialniDownloader(logger, Downloader())
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
            if len(links) > 1:
                publishedDate = datetime.strptime(item['published'][:-6], '%a, %d %b %Y %H:%M:%S')
                yield Episode(publishedDate, item['links'][1]['href'])

    def _findAllNewEpisodes(self, lastDownloadedEpisode):
        cleanEpisodeName = lastDownloadedEpisode[self.FilePrefixSize:].lower()

        results = []
        for link in self._getNextEpisode():
            href = link.getLink().lower()
            if cleanEpisodeName in href:
                return results

            results.append(link)

        return results

    def _createForLink(self, episode):
        onlyFileName = episode.getLink().rpartition('/')[-1]
        return '[%s] %s' % (episode.getPublishDate().strftime('%Y%m%d'), onlyFileName)
