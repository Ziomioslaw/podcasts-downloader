import feedparser

from datetime import datetime
from mp3fromrss import Mp3FromRSSDownloader
from mp3fromrss import Episode

class WithDateOnBeginingDownloader(Mp3FromRSSDownloader):
    FilePrefixSize = 11 # File has additional prefix: '[YYYYMMDD] '

    def __init__(self, logger, rssLink, downloader):
        Mp3FromRSSDownloader.__init__(self, logger, downloader)
        self.rssLink = rssLink

    def _getNextEpisode(self):
        feed = feedparser.parse(self.rssLink)
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
        onlyFileNameWithParamaters = episode.getLink().rpartition('/')[-1]
        onlyFileName = onlyFileNameWithParamaters.rpartition('?')[0]

        return '[%s] %s' % (episode.getPublishDate().strftime('%Y%m%d'), onlyFileName)

