import feedparser
from datetime import datetime

from mp3fromrss import Mp3FromRSSDownloader
from mp3fromrss import FindAndDownloadMissing
from mp3fromrss import DownloadedEpisodesManager
from mp3fromrss import Episode

class Squanch(FindAndDownloadMissing):
    def __init__(self, logger, path):
        FindAndDownloadMissing.__init__(
            self,
            logger,
            DownloadedEpisodesManager(path),
            SquanchDownloader(logger)
        )

    def _getName(self):
        return "Squanch"

class SquanchDownloader(Mp3FromRSSDownloader):
    MainRSSLink = 'http://squanch.libsyn.com/rss'
    DownloadServerDirectory = 'http://dts.podtrac.com/redirect.mp3/traffic.libsyn.com/squanch/'
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
