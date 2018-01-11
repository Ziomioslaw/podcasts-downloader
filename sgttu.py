from mp3fromrss import FindAndDownloadMissing
from mp3fromrss import DownloadedEpisodesManager
from mp3fromrss import Downloader
from mp3fromrss import FeedReader
from mp3fromrss import LiveFeedSource

class SGTTU(FindAndDownloadMissing):
    DownloadServerDirectory = 'http://media.libsyn.com/media/skepticsguide/'
    MainRSSLink = 'http://www.theskepticsguide.org/feed/rss.aspx'

    def __init__(self, logger, path):
        FindAndDownloadMissing.__init__(
            self,
            logger,
            DownloadedEpisodesManager(path),
            Downloader(),
            FeedReader(LiveFeedSource(self.MainRSSLink))
        )

    def _getName(self):
        return "SGTTU"

    def _createForLink(self, episode):
        return episode.getLink()[len(self.DownloadServerDirectory):]
