import feedparser
from datetime import datetime

from mp3fromrss import Mp3FromRSSDownloader
from mp3fromrss import FindAndDownloadMissing
from mp3fromrss import DownloadedEpisodesManager
from mp3fromrss import Downloader
from mp3fromrss import Episode

class SGTTU(FindAndDownloadMissing):
    def __init__(self, logger, path):
        FindAndDownloadMissing.__init__(
            self,
            logger,
            DownloadedEpisodesManager(path),
            SGTTUDownloader(logger, Downloader())
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
            publishedDate = datetime.strptime(item['published'][:-6], '%a, %d %b %Y %H:%M:%S')
            link = item['links'][0]['href']
            yield Episode(publishedDate, link)

    def _findAllNewEpisodes(self, lastDownloadedEpisode):
        results = []
        for episode in self._getNextEpisode():
            if lastDownloadedEpisode in episode.getLink():
                return results

            results.append(episode)

        return results

    def _createForLink(self, episode):
        return episode.getLink()[len(self.DownloadServerDirectory):]

